# AWS Cloud Architecture Portfolio

## 1. 目的 - Objective

未経験からAWSクラウドエンジニアとしての転職を目指し、  
**実務レベルのインフラ構築・自動化・監視・説明スキル**を証明するためのポートフォリオです。

GUIでの手動構築から始まり、TerraformによるIaC、サーバレス構成、CI/CD、監視設計まで網羅。  
さらに、構成意図をNotion/PDFで言語化することで「技術を説明できる力」も証明します。

---

## 2. 技術スタック - Tech Stack

- **AWSサービス**：VPC / EC2 / S3 / RDS / Route53 / IAM / Lambda / API Gateway / DynamoDB / CloudWatch / SNS
- **IaC**：Terraform
- **CI/CD**：GitHub Actions / AWS CodePipeline
- **構成図作成**：draw.io / Canva

---

## 3. ロードマップ - Roadmap

| STEP | 内容                              | 完了状況 |
|------|-----------------------------------|----------|
| STEP 1 | GUI構築（VPC, EC2, S3など）         | ✅ 完了 |
| STEP 2 | TerraformによるIaC構成              | ✅ 完了 |
| STEP 3 | サーバレス構成（Lambda等）           | ✅ 完了 |
| STEP 4 | CI/CD＆監視設計                     | ✅ 完了 |
| STEP 5 | Notion/PDFによる資料整備             | ✅ 完了 |
| STEP 6 | ECS/コンテナ構成                     | ✅ 完了 |
| STEP 7 | 企業別カスタム構成                   | ⏳ 準備中 |
| STEP 8 | 実案件再現                           | ⏳ 準備中 |

---

## 4. 各ステップの概要 - Step Overview

### 4-1. Step 1：GUI構成（VPC / EC2 / S3 など）

AWSマネジメントコンソールを用いて、以下のGUI構成を設計・構築しました：

- VPC内のPublic / Privateサブネット分離
- EC2 → RDSへの安全な通信経路の確保
- NAT Gateway / IGWを通じた外部接続
- S3・CloudWatch・Route 53 との連携設計

📄 詳細・構成図は [`step1_gui_build/README.md`](./step1_gui_build/README.md)

---

### 4-2. Step 2：Terraform構成（VPC / Subnet / Route Table）

TerraformによりStep1と同等の構成をコードで再現（Infrastructure as Code）しました：

- 再現性の高いVPC基盤構成（Public Subnet＋IGW＋Route Table）
- AWS CLI + VSCode + GitHub連携による実行証明
- GUIとコード両方のスキルを証明する内容に構成

📄 詳細は [`step2_terraform_build/README.md`](./step2_terraform_build/README.md)

---

### 4-3. Step 3：サーバレス構成（Lambda / API Gateway）

Terraformを用いて、**API GatewayとLambdaによる完全サーバレス構成**を構築しました：

- Lambda関数をTerraformで定義・デプロイ
- API GatewayのHTTPルートと統合設定（Proxy統合）
- `terraform apply` により即時URL発行
- ブラウザアクセスで `Hello from Lambda!` を確認
- GUI上でもLambda / API Gatewayの存在を確認
- CloudWatch LogsにLambda実行ログが記録されていることも確認済み

📄 詳細・コード・構成図・実行結果は  
[`step3_serverless_build/README.md`](./step3_serverless_build/README.md)

---

### 4-4. Step 4：CI/CD ＆ 監視設計（GitHub Actions / CloudWatch）

GitHub Push → Lambda自動更新 → 実行ログ → メトリクス → エラー検知 → メール通知  
という運用の自動化と可視化フローを構築。

- `.github/workflows/deploy.yml` でCI/CD構成
- CloudWatch Logsで実行ログを出力・確認
- CloudWatch Metricsで呼び出し回数／実行時間をグラフ化
- Errors ≥ 1 のアラームでSNS経由メール通知を構成
- アーキテクチャ構成図をdraw.ioで可視化

📄 実装内容とスクリーンショットは  
[`step4_ci_cd_build/README.md`](./step4_ci_cd_build/README.md)

---

### 4-5. Step 5：構成意図のドキュメント化（Notion / PDF）

構成意図・技術選定理由・設計思想・応用力などをNotionとPDFで文章化。

- 採用担当者にも伝わる「なぜその構成にしたか？」を明示
- 他の構成との比較・応用可能性まで記述
- PDF化して提出用資料としても活用可能

📄 構成意図ドキュメントはこちら  
[`step5_documentation/README.md`](./step5_documentation/README.md)

---

### 4-6. Step 6：ECS / Fargate + CI/CD + CloudWatch

FlaskアプリをDockerでコンテナ化し、ECRにPush → ECS (Fargate) で本番デプロイ。  
さらに、GitHub ActionsでCI/CDを構築し、CloudWatchでログ出力とCPU使用率の監視まで対応。

- Flaskアプリ → Docker化
- ECR → ECS（Fargate）にイメージを展開
- ALB → Target Group → ECS ServiceへのルーティングをTerraformで構築
- GitHub ActionsのPushトリガーで自動ビルド・デプロイ（deploy-ecs.yml）
- CloudWatch Logsへアプリログを出力、80%以上のCPU使用率でアラーム設定
- draw.ioにてアーキテクチャ構成図を作成（後日反映）

📄 詳細・構成図・ログなどは  
[`step6_ecs_fargate_build/README.md`](./step6_ecs_fargate_build/README.md)

---

## 5. その他

- 各ステップごとにコードと構成図を整理
- 最終的にNotion/PDFにて「構成意図 × 設計思想 × 再現性」を採用向けに提出済み

---

> 本ポートフォリオは、「作れる力 × 再現できる力 × 説明できる力」の三位一体を証明するものです。
