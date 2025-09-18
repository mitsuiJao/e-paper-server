#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>

#define ORIGINAL_WIDTH 32
#define ORIGINAL_HEIGHT 32
#define SCALE_FACTOR 4

#define ENLARGED_WIDTH (ORIGINAL_WIDTH * SCALE_FACTOR)
#define ENLARGED_HEIGHT (ORIGINAL_HEIGHT * SCALE_FACTOR)

// 拡大後のビットマップ (128x128)
int enlarged_bitmap[ENLARGED_HEIGHT][ENLARGED_WIDTH];

//--- ユーティリティ関数
int parse_xbm_data(FILE *fp, unsigned char *data_array) {
    char line[256];
    int byte_count = 0;

    // ヘッダー部を読み飛ばす
    while (fgets(line, sizeof(line), fp)) {
        if (strstr(line, "static char")) {
            break;
        }
    }

    if (feof(fp)) {
        fprintf(stderr, "Error: XBM data not found.\n");
        return 0;
    }

    // データ部分を解析
    while (fgets(line, sizeof(line), fp)) {
        // } が見つかったら終了
        if (strstr(line, "}")) {
            break;
        }

        char *token = strtok(line, ",; \n\r");
        while (token) {
            if (strstr(token, "0x")) {
                data_array[byte_count++] = (unsigned char)strtol(token, NULL, 16);
            }
            token = strtok(NULL, ",; \n\r");
        }
    }
    return byte_count;
}

int get_pixel_from_xbm_data(unsigned char *data, int x, int y) {
    int byte_index = y * (ORIGINAL_WIDTH / 8) + (x / 8);
    int bit_index = x % 8;
    unsigned char byte = data[byte_index];
    return (byte >> bit_index) & 1;
}

void enlarge_bitmap_from_data(unsigned char *original_data) {
    for (int i = 0; i < ORIGINAL_HEIGHT; i++) {
        for (int j = 0; j < ORIGINAL_WIDTH; j++) {
            int pixel_value = get_pixel_from_xbm_data(original_data, j, i);
            for (int k = 0; k < SCALE_FACTOR; k++) {
                for (int l = 0; l < SCALE_FACTOR; l++) {
                    enlarged_bitmap[i * SCALE_FACTOR + k][j * SCALE_FACTOR + l] = pixel_value;
                }
            }
        }
    }
}

void write_enlarged_xbm(const char *filepath) {
    FILE *fp = fopen(filepath, "w");
    if (!fp) {
        perror("Failed to open output file");
        return;
    }

    fprintf(fp, "#define enlarged_width %d\n", ENLARGED_WIDTH);
    fprintf(fp, "#define enlarged_height %d\n", ENLARGED_HEIGHT);
    fprintf(fp, "static unsigned char enlarged_bits[] = {\n");

    int byte_count = 0;
    int bytes_per_row = ENLARGED_WIDTH / 8;
    int total_bytes = bytes_per_row * ENLARGED_HEIGHT;

    for (int i = 0; i < ENLARGED_HEIGHT; i++) {
        fprintf(fp, "   ");
        for (int j = 0; j < bytes_per_row; j++) {
            unsigned char byte = 0;
            for (int k = 0; k < 8; k++) {
                if (enlarged_bitmap[i][j * 8 + k] == 1) {
                    byte |= (1 << k);
                }
            }
            fprintf(fp, "0x%02x", byte);
            byte_count++;
            
            if (byte_count < total_bytes) {
                fprintf(fp, ",");
            }
            // 1行あたり10バイトで改行
            if (j % 10 == 9) {
                fprintf(fp, "\\\n   ");
            } else {
                 fprintf(fp, " ");
            }
        }
        fprintf(fp, "\n");
    }
    fprintf(fp, "};\n");
    fclose(fp);
}

int main() {
    char input_path[256];
    char output_dir[256];
    char output_path[256];
    unsigned char original_data[ORIGINAL_WIDTH * ORIGINAL_HEIGHT / 8];
    
    // 出力ディレクトリ名を設定
    sprintf(output_dir, "%d", ENLARGED_WIDTH);

    // 出力ディレクトリを作成
    if (mkdir(output_dir, 0755) != 0) {
        if (errno != EEXIST) {
            perror("Failed to create directory");
            return 1;
        }
    }

    while (fgets(input_path, sizeof(input_path), stdin)) {
        // 末尾の改行を削除
        input_path[strcspn(input_path, "\n")] = 0;

        FILE *fp = fopen(input_path, "r");
        if (!fp) {
            perror("Failed to open input file");
            continue;
        }

        // XBMデータを解析して配列に格納
        int byte_count = parse_xbm_data(fp, original_data);
        fclose(fp);

        if (byte_count == 0) {
            continue;
        }

        // 拡大処理を実行
        enlarge_bitmap_from_data(original_data);

        // 出力パスを作成 (例: 128/sun.xbm)
        const char *filename = strrchr(input_path, '/');
        if (filename) {
            filename++;
        } else {
            filename = input_path;
        }
        sprintf(output_path, "%s/%s", output_dir, filename);

        // 拡大後のデータをファイルに出力
        write_enlarged_xbm(output_path);

        printf("Processed %s -> %s\n", input_path, output_path);
    }
    
    return 0;
}