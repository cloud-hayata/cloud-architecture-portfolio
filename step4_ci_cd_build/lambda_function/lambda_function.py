# Lambda関数にわざとエラーを仕込む
def lambda_handler(event, context):
    raise Exception("Forced Error for Alarm Test!")
