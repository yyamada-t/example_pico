# example_pico - 天気表示プロジェクト

## 機器
- Raspberry Pi Pico W (x1)
- SSD1306(128x32) OLED ディスプレイ (x1)
- タクトスイッチ (x1)

## 機能
- WiFi接続して天気情報をOpenWeatherMap APIから取得
- OLEDディスプレイに現在の天気情報を表示
- タクトスイッチを押すことで天気情報を手動更新
- 5分ごとに自動的に天気情報を更新

## 開発環境
- VSCode
- 拡張機能 Raspberry Pi Pico
- MicroPython

## 電源
- Raspberry Pi Pico WのUSB-microBから供給

## 接続
### SSD1306 OLED ディスプレイ
- VCC → Pin 36 (3.3V)
- GND → Pin 38 (GND)
- SDA → Pin 6 (GP4)
- SCL → Pin 7 (GP5)

### タクトスイッチ
- 一端 → Pin 20 (GP15)
- 他端 → Pin 38 (GND)

## セットアップ
詳細なセットアップ手順は `setup_instructions.md` を参照してください。

## ファイル構成
- `main.py` - メインプログラム
- `config.py` - WiFi設定とAPI設定
- `display.py` - OLED ディスプレイ制御
- `network.py` - WiFi接続と天気API通信
- `setup_instructions.md` - 詳細セットアップ手順
- `requirements.txt` - 必要なライブラリ一覧

## 必要な設定
1. OpenWeatherMap APIキーの取得
2. `config.py`でWiFi設定とAPIキーを設定
3. `ssd1306.py`ライブラリのインストール
