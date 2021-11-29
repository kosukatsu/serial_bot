import json
import argparse

import serial
import yaml
import requests

def load_yaml(file):
    with open(file,"r") as f:
        read_data=yaml.safe_load(f)
    return read_data

def main(conf):
    # シリアル通信
    readSer = serial.Serial(conf["serial_port"], conf["bps"], timeout=3)
    try:
        while True:
            line = readSer.readline() 
            if line != b"":
                time = float(line)
                print(time)
                try:
                    requests.post(
                        conf["web_hook_url"],
                        data=json.dumps(
                            {
                                "text": str(time),
                                "icon_emoji": ":stopwatch:",
                                "username": "ストップウォッチ",
                            }
                        ),
                    )
                except: # 通信できなかったとき
                    print("requests error")
    finally: # 終了時
        readSer.close()


if __name__ == "__main__":
    parser=argparse.ArgumentParser()

    parser.add_argument("conf",help="conf yaml file")
    args=parser.parse_args()
    conf=load_yaml(args.conf) 
    main(conf)
