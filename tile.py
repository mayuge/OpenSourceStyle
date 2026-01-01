from PIL import Image
import os

# ==========================
# 設定
# ==========================

input_image_path = "gradient.png"
output_tiles_root = "tiles"

tile_size_pixels = 256
minimum_zoom = 0
maximum_zoom = 20

# ==========================
# 画像読み込み
# ==========================

source_image = Image.open(input_image_path).convert("RGBA")

# タイルサイズにリサイズ（拡大しない）
source_image = source_image.resize(
    (tile_size_pixels, tile_size_pixels),
    Image.BILINEAR
)

# ==========================
# タイル生成
# ==========================

for zoom_level in range(minimum_zoom, maximum_zoom + 1):
    number_of_tiles_per_axis = 2 ** zoom_level

    for tile_x in range(number_of_tiles_per_axis):
        for tile_y in range(number_of_tiles_per_axis):

            tile_directory_path = os.path.join(
                output_tiles_root,
                str(zoom_level),
                str(tile_x)
            )

            os.makedirs(tile_directory_path, exist_ok=True)

            tile_file_path = os.path.join(
                tile_directory_path,
                f"{tile_y}.png"
            )

            source_image.save(tile_file_path, "PNG")

    print(f"zoom {zoom_level} 完了")

print("すべてのタイル生成が完了しました")
