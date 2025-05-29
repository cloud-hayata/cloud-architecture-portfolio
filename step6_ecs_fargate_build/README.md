# Step6: FlaskアプリをECS/Fargateに本番デプロイ＋CI/CD＋監視構築

このプロジェクトは、AWS上で **FlaskアプリケーションをDockerでコンテナ化**し、  
**ECS / Fargate に本番環境レベルでデプロイ → GitHub ActionsでCI/CD → CloudWatchで監視**までを一貫して構築するポートフォリオです。

---

## 1. 使用技術スタック

| カテゴリ       | 使用サービス / ツール                     |
|--------------|------------------------------------------|
| インフラ構成   | VPC, Subnet, IGW, Security Group         |
| コンテナ実行環境 | Docker, ECS (Fargate), ECR               |
| 負荷分散       | ALB (Application Load Balancer)         |
| 自動デプロイ   | GitHub Actions                          |
| ログ & 監視    | CloudWatch Logs, CloudWatch Alarms      |

---

## 2. アーキテクチャ概要図

GitHub Actions による CI/CD パイプラインから  
ECS / Fargate、ALB経由のアクセス、CloudWatch監視までを網羅した構成図です。

図内に含まれる構成要素：
- GitHub Actions による Docker Build & ECS 更新
- ECR リポジトリとイメージ管理
- ECS Cluster / Task / Container の実行環境
- ALB → Target Group → ECS へのルーティング
- CloudWatch Logs & CPU Alarm による監視

📸 構成図:
![アーキテクチャ図](images/step6_architecture.png)

---

## 3. 構築ステップと成果物

### 3-1. FlaskアプリのDocker化

- `Dockerfile` と `app.py` を用意し、ローカルでビルド＆実行
- コンテナ起動とブラウザ表示確認

📸 スクリーンショット:
- Dockerイメージをビルドしたログ  
  ![docker build](images/step6_docker_build.png)
  
- ビルドしたコンテナを8080番ポートで起動  
  ![docker run](images/step6_docker_run.png)
  
- ブラウザで `localhost:8080` にアクセスしてアプリを表示  
  ![ブラウザ表示確認](images/step6_browser_access.png)

---

### 3-2. ECRへのPush

- AWS CLIでECRにログイン
- DockerイメージをECRにPush

📸 スクリーンショット:
![ECR Push](images/step6_ecr_push.png)

---

### 3-3. ECS / Fargate構築（Terraform）

- VPC, Subnet, SG, ECS Cluster, Task定義、Serviceなどを構築

📸 スクリーンショット:
- VPCとSGをTerraformで構築  
  ![VPC + SG](images/step6_ecs_vpc_sg.png)
  
- ECSクラスター作成完了  
  ![ECS Cluster](images/step6_ecs_cluster.png)
  
- Fargateタスクが実行中  
  ![Task Running](images/step6_ecs_task_running.png)

---

### 3-4. ALB構成とアクセス確認

- TerraformでALB（Application Load Balancer）とTarget Groupを構築し、ECS Serviceと接続
- ALBのDNS名にアクセスし、ECS上のFlaskアプリがブラウザで動作していることを確認

📸 スクリーンショット:

- TerraformでALBを構築し、完了したログ（PowerShell出力）  
  ![ALB構築ログ](images/step6_alb_access.png)

- ALBのDNS名にブラウザからアクセスし、Flaskアプリが表示された画面  
  ![ALBアクセス確認](images/step6_final_result.png)

---

### 3-5. GitHub ActionsでCI/CD構築

- `deploy-ecs.yml` により、自動ビルド＆デプロイを実現
- Push → Build → ECR Push → ECS Serviceを更新

---

### 3-6. CloudWatchによる監視

- CloudWatch Logs:
  - `/ecs/step6-flask-log-group` にログを出力
- CloudWatch Alarm:
  - `high-cpu-usage-alarm`（CPU使用率が80%を超えると通知）

---

## 4. デプロイ確認

- ALB経由でアプリにアクセスし、 `Hello from Flask inside Docker!` を確認済

📸 スクリーンショット:

![ALBアクセス確認](images/step6_final_result.png)

---

## 5. ディレクトリ構成（概要）

```plaintext
cloud-architecture-portfolio/
├── .github/
│   └── workflows/
│       └── deploy-ecs.yml               # GitHub Actionsによる自動デプロイ
├── step6_ecs_fargate_build/
│   ├── docker/
│   │   ├── app.py                       # Flaskアプリ本体
│   │   ├── Dockerfile                   # Docker構成
│   │   └── requirements.txt             # 依存ライブラリ定義
│   ├── terraform/
│   │   └── main.tf                      # VPC〜ECS構成を定義したTerraformコード
│   ├── images/
│   └── README.md                        # 本構成の解説ドキュメント
```

---

## 6. 今後の改善ポイント

- ALBのHTTPS対応（ACM + Route53）
- ECS Auto Scaling導入
- CloudWatch Alarm → SNS or Slack通知連携
- Secrets ManagerでECSの環境変数管理
- デプロイ結果をGitHub Actionsから通知

---

## 7. この構成について

このインフラ構成は、AWSクラウドエンジニア転職を目指すポートフォリオとして個人で構築しました。  
Terraform / ECS / ALB / GitHub Actions / CloudWatch など、本番運用レベルの構成力を証明することを目的としています。

設計レビュー・改善提案など、大歓迎です！
