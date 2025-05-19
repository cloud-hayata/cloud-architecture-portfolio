# AWS Cloud Architecture Portfolio

## 1. 目的 - Objective
未経験からAWSクラウドエンジニアとしての転職を目指し、実務レベルのインフラ構築スキルを証明するためのポートフォリオです。

GUIでの手動構築から始まり、TerraformによるIaC、Serverless構成、CI/CD、監視設計まで網羅しています。

## 2. 技術スタック - Tech Stack
- **AWSサービス**：VPC / EC2 / S3 / RDS / Route53 / IAM / Lambda / API Gateway / DynamoDB / CloudWatch / SNS
- **IaC**：Terraform
- **CI/CD**：GitHub Actions / AWS CodePipeline
- **構成図作成**：draw.io / Canva

## 3. ロードマップ - Roadmap
| STEP | 内容 | 完了状況 |
|------|------|----------|
| STEP 1 | GUI構築（VPC, EC2, S3など） | 🔄 進行中 |
| STEP 2 | TerraformによるIaC構成 | ⏳ 準備中 |
| STEP 3 | サーバレス構成（Lambda等） | ⏳ 準備中 |
| STEP 4 | CI/CD＆監視設計 | ⏳ 準備中 |
| STEP 5 | Notion/PDFによる資料整備 | ⏳ 準備中 |
| STEP 6 | ECS/コンテナ構成 | ⏳ 準備中 |
| STEP 7 | 企業別カスタム構成 | ⏳ 準備中 |
| STEP 8 | 実案件再現 | ⏳ 準備中 |

## 🔍 Step 1 詳細：GUI構成（VPC / EC2 / S3 など）

VPC内のPublic / Privateサブネット分離、EC2 → RDSへの通信、  
NAT Gateway / IGW経由の外部接続、S3・CloudWatch・Route 53連携などを構築。

👉 詳細・構成図は [step1_gui_build/README.md](./step1_gui_build/README.md) に記載しています。

## その他
- 各ステップごとにコードと構成図を格納予定です
- 最終的にNotion/PDFにて構成意図・設計思想をまとめ、採用資料として活用します
