# Raspberry Pi Pico W 天気表示プロジェクト セットアップ手順

## 必要なもの
- Raspberry Pi Pico W (MicroPython UF2インストール済み)
- SSD1306 OLED ディスプレイ (128x32)
- タクトスイッチ
- ブレッドボードとジャンパーワイヤー

## ハードウェア接続

### SSD1306 OLED ディスプレイ
```
SSD1306    →    Pico W
VCC        →    Pin 36 (3.3V)
GND        →    Pin 38 (GND)
SDA        →    Pin 6  (GP4)
SCL        →    Pin 7  (GP5)
```

### タクトスイッチ
```
スイッチ    →    Pico W
一端       →    Pin 20 (GP15)
他端       →    Pin 38 (GND)
```

## ソフトウェアセットアップ

### 1. MicroPythonライブラリのインストール
1. `ssd1306.py`をダウンロード:
   - https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py
2. Raspberry Pi Pico Wにアップロード

### 2. 設定ファイルの編集
`config.py`を編集して以下を設定:
```python
WIFI_SSID = "あなたのWiFi名"
WIFI_PASSWORD = "あなたのWiFiパスワード"
OPENWEATHER_API_KEY = "あなたのAPIキー"
```

### 3. OpenWeatherMap APIキーの取得
1. https://openweathermap.org/ にアクセス
2. 無料アカウントを作成
3. APIキーを取得
4. `config.py`に設定

### 4. ファイルのアップロード
以下のファイルをRaspberry Pi Pico Wにアップロード:
- `main.py`
- `config.py`
- `display.py`
- `network.py`
- `ssd1306.py`

## 使用方法

### 起動
1. Raspberry Pi Pico WをUSBで電源に接続
2. 自動的にプログラムが開始
3. WiFi接続後、天気情報が表示される

### 操作
- **タクトスイッチ押下**: 天気情報を手動更新
- **自動更新**: 5分ごとに自動的に天気情報を更新

### 表示内容
- 1行目: 都市名
- 2行目: 気温 (°C)
- 3行目: 天気の説明

## トラブルシューティング

### WiFi接続できない
- SSID/パスワードを確認
- WiFiの電波強度を確認
- 2.4GHz帯のWiFiを使用しているか確認

### 天気情報が表示されない
- APIキーが正しく設定されているか確認
- インターネット接続を確認
- APIの使用制限を確認 (無料版は1日1000回まで)

### ディスプレイに何も表示されない
- 配線を確認
- I2Cアドレスを確認 (通常は0x3C)
- 電源供給を確認

## カスタマイズ

### 表示する都市の変更
`config.py`の`DEFAULT_CITY`と`DEFAULT_COUNTRY`を変更:
```python
DEFAULT_CITY = "Osaka"
DEFAULT_COUNTRY = "JP"
```

### 更新間隔の変更
`config.py`の`DISPLAY_UPDATE_INTERVAL`を変更 (秒単位):
```python
DISPLAY_UPDATE_INTERVAL = 600  # 10分間隔
```

### ボタンピンの変更
`main.py`のボタンピン設定を変更:
```python
self.button = Pin(14, Pin.IN, Pin.PULL_UP)  # GP14を使用
```
