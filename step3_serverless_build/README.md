# Step3: Serverless Architecture (Terraform)

## 1. 概要 - Overview

本ステップでは、**API Gateway + Lambda** をTerraformで構築し、完全サーバレスなアーキテクチャを再現しています。  
採用担当者や技術者が一目で理解できるよう、構成図とコードによって**「設計力 × 実装力 × 再現性」**を証明します。

---

## 2. 構成図 - Architecture Diagram

以下は本構成の全体像です。（クリックで拡大表示可能）

![serverless_architecture_diagram](./serverless_architecture_diagram.png)

- クライアントからのリクエストをAPI Gatewayで受け取り、Lambdaに転送
- Lambdaは「Hello from Lambda!」を返す簡易構成
- CloudWatch Logsに自動ログ出力

---

## 3. 使用Terraformリソース - Main Resources

| リソース名                     | 説明                            |
|------------------------------|---------------------------------|
| `aws_lambda_function`        | Lambda本体                      |
| `aws_apigatewayv2_api`       | HTTP API Gateway                |
| `aws_apigatewayv2_integration` | API GatewayとLambdaの接続設定  |
| `aws_apigatewayv2_route`     | エンドポイント（例：/hello）   |
| `aws_apigatewayv2_stage`     | ステージ（例：dev）            |
| `aws_lambda_permission`      | API Gateway → Lambda呼び出し権限 |
| `aws_iam_role`               | Lambda実行用ロール             |

---

## 4. Lambda関数内容（Python例）

```python
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello from Lambda!"
    }
```
