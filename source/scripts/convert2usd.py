# https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_asset-converter.html
#
import os
import argparse
import omni.kit.asset_converter as converter
import asyncio

def progress_callback(current_step: int, total: int):
    # Show progress
    print(f"{current_step} of {total}")

async def convert(input_asset_path, output_asset_path):
    task_manager = converter.get_instance()
    task = task_manager.create_converter_task(input_asset_path, output_asset_path, progress_callback)
    success = await task.wait_until_finished()
    if not success:
        detailed_status_code = task.get_status()
        detailed_status_error_string = task.get_error_message()

parser = argparse.ArgumentParser(
                    prog='convert2usd',
                    description='Converts OBJ files to USD format')
parser.add_argument('path', help='path to file or directory')
args = parser.parse_args()

path = args.path
if os.path.isfile(path):
    asyncio.run(convert(path, path + ".usd"))
else:
    for fileName in sorted(os.listdir(path)):
        if not fileName.endswith(".obj"):
            continue
        filePath = path + "/" + fileName
        print("Converting " + filePath)
        asyncio.run(convert(filePath, filePath + ".usd"))
