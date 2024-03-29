## セットアップ
入力ファイル（.csvまたは.txt）をこのフォルダーに置いてください。\
他のCSVファイルからデータをインポートする場合は、このフォルダーに置いてください。\
必ずこのフォルダーに移動してからスクリプトを実行してください。

## 使い方
./generator.sh <行数> <ファイル名>.csv <乱数シード(任意)>

## CSVファイル
コラム名、コラム名、コラム名\
データ定義、データ定義、データ定義

## TXTファイル
// コメント："//"で始める行は無視されます。 \
コラム名 \
データ定義 \
コラム名 \
データ定義 \
コラム名 \
データ定義

### FIXED VALUE
VALUE(VALUE)　固定値 \
SERIAL(START)　シークエンス \
BLANK　空白 \
NULL \
FROM_TABLE(CSV_FILE COLUMN_NAME REPEAT=TRUE/FALSE)　CSVファイルからデータ読み込む（順番通り）（REPEAT=繰り返し） \
RANDOM_FROM_TABLE(CSV_FILE COLUMN_NAME)　CSVファイルからデータ読み込む（ランダム） \
LIST_ORD(VAL1 VAL2...)　リスト（順番通り、繰り返し） \
LIST_RAND(VAL1 VAL2...)　リスト（ランダム） \
COPY(COLUMN)　作成済みのコラムをコピー 

### NUMBERS
ZERO \
ONE \
RANDOM(START END INTERVAL)　ランダむ数字　(スタート、エンド、間隔) \
ZERO_PADDED(LENGTH START)　ゼロ埋めのシークエンス　LENGTH＝桁数　例：001 \
RANDOM_ZERO_PADDED(LENGTH START END INTERVAL)　ゼロ埋めのランダム数字　LENGTH＝桁数　例：0027 \
RANDOM_PRICE(START END INTERVAL)　ランダム価格　例：20000.000

### DATETIME
TIMESTAMP_NOW　今のタイムスタンプ　（日付と時、分、秒） \
TIMESTAMP_TODAY　今日の日付 \
TIMESTAMP_DATE(START_DATE END_DATE)　ランダム日付 \
TIMESTAMP_SECONDS(START_DATE END_DATE)　ランダムタイムスタンプ　（秒まで） TIMESTAMP()も使えます \
TIMESTAMP_MILLIS(START_DATE END_DATE)　ランダムタイムスタンプ　（ミリ秒まで）

### SYSTEM
USER_AGENT \
IP_ADDRESS

### PERSON
ID　シークエンス \
USERNAME　未実装 \
PASSWORD　ランダムパスワード \
PASSWORD_HASH 未実装 \
NAME_FAMILY \
NAME_FIRST \
NAME_FULL \
NAME_FAMILY_KN　未実装 \
NAME_FIRST_KN　未実装 \
NAME_FULL_KN　未実装 \
NAME_FAMILY_EN　未実装 \
NAME_FIRST_EN　未実装 \
NAME_FULL_EN　未実装 \
DATE_OF_BIRTH　生年月日 \
AGE　未実装 \
SEX　男か女 \
SEX_AS_NUM　0か１ \
ADDRESS_ZIP　郵便番号 \
ADDRESS_FULL 住所 \
ADDRESS_COUNTRY　未実装 \
ADDRESS_PREFECTURE　未実装 \
ADDRESS_CITY　未実装 \
ADDRESS_CHOME　未実装 \
ADDRESS_BANCHI　未実装 \
ADDRESS_NUMBER　未実装 \
ADDRESS_BUILDING　未実装 \
ADDRESS_ROOM_NO　未実装 \
PHONE_HOME　未実装 \
PHONE_WORK　未実装 \
PHONE_MOBILE　未実装 \
EMAIL_WORK　未実装 \
EMAIL_PERSONAL　未実装 \
PROFESSION　未実装 \
NATIONALITY　未実装 \
COMPANY_NAME　未実装 \
COMPANY_ROLE　未実装 \
COMPANY_DIVISION　未実装

### COMPANY
INDUSTRY　未実装 \
COMPANY_NAME　未実装 \
COMPANY_DIVISION　未実装

