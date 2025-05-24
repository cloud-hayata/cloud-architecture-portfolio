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
| STEP 1 | GUI構築（VPC, EC2, S3など） | ✅ 完了 |
| STEP 2 | TerraformによるIaC構成 | ✅ 完了 |
| STEP 3 | サーバレス構成（Lambda等） | ⏳ 準備中 |
| STEP 4 | CI/CD＆監視設計 | ⏳ 準備中 |
| STEP 5 | Notion/PDFによる資料整備 | ⏳ 準備中 |
| STEP 6 | ECS/コンテナ構成 | ⏳ 準備中 |
| STEP 7 | 企業別カスタム構成 | ⏳ 準備中 |
| STEP 8 | 実案件再現 | ⏳ 準備中 |

## 4. 各ステップの概要 - Step Overview

### 4-1. Step 1：GUI構成（VPC / EC2 / S3 など）

AWSマネジメントコンソールを用いて、以下のGUI構成を設計・構築しました。

- VPC内のPublic / Privateサブネット分離
- EC2 → RDSへの安全な通信経路の確保
- NAT Gateway / IGWを通じた外部接続
- S3・CloudWatch・Route 53 との連携設計

📄 詳細・構成図は [`step1_gui_build/README.md`](./step1_gui_build/README.md) に記載しています。

---

### 4-2. Step 2：Terraform構成（VPC / Subnet / Route Table）

TerraformによりStep1と同等の構成をコードで再現（Infrastructure as Code）しました。

- 再現性の高いVPC基盤構成（Public Subnet＋IGW＋Route Table）
- AWS CLI + VSCode + GitHub連携による実行証明
- GUIとコード両方のスキルを証明する内容に構成

📄 詳細は [`step2_terraform_build/README.md`](./step2_terraform_build/README.md) に記載

---

## 5. その他

- 各ステップごとにコードと構成図を整理
- 最終的にNotion/PDFにて「構成意図 × 設計思想 × 再現性」を採用向けに提出予定

---

> 本ポートフォリオは、「作れる力 × 再現できる力 × 説明できる力」の三位一体を証明するものです。
