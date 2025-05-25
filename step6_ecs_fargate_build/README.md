# Step6: ECS / Fargate + CI/CD + CloudWatch - README

このプロジェクトは、AWS上で本番環境レベルのWebアプリ構成を構築・自動化・監視するための学習用ポートフォリオです。  
FlaskアプリをDockerでコンテナ化し、Amazon ECS / Fargate上で稼働させ、GitHub ActionsによるCI/CDおよびCloudWatchによるログ・アラーム監視までを網羅しています。

---

## 1. 使用技術スタック

| カテゴリ     | 使用サービス / ツール                    |
|------------|----------------------------------------|
| インフラ     | VPC, Subnet, IGW, SG                   |
| コンテナ     | Docker, ECS (Fargate), ECR             |
| ロードバランサー | ALB (Application Load Balancer)      |
| CI/CD      | GitHub Actions                          |
| モニタリング | CloudWatch Logs, CloudWatch Alarms     |

---

## 2. アーキテクチャ概要図

![step6_final_result](./step6_ecs_fargate_build/step6_final_result.png)

---

## 3. 構築ステップと成果物

### 3-1. FlaskアプリのDocker化

- `Dockerfile` と `app.py` を用意し、ローカルでビルド＆実行
- コンテナ起動とブラウザ表示確認

📸 スクリーンショット:
- ![docker build](./step6_ecs_fargate_build/step6_docker_build.png)
- ![docker run](./step6_ecs_fargate_build/step6_docker_run.png)
- ![ブラウザ表示確認](./step6_ecs_fargate_build/step6_browser_access.png)

---

### 3-2. ECRへのPush

- AWS CLIでECRにログイン
- DockerイメージをECRにPush

📸 スクリーンショット:
- ![ECR Push](./step6_ecs_fargate_build/step6_ecr_push.png)

---

### 3-3. ECS / Fargate構築（Terraform）

- VPC, Subnet, SG, ECS Cluster, Service, Task定義などをTerraformで構築

📸 スクリーンショット:
- ![VPC + SG](./step6_ecs_fargate_build/step6_ecs_vpc_sg.png)
- ![ECS Cluster](./step6_ecs_fargate_build/step6_ecs_cluster.png)
- ![Task Running](./step6_ecs_fargate_build/step6_ecs_task_running.png)

---

### 3-4. ALB構成とアクセス確認

- ALB → Target Group → ECS Serviceに接続
- ドメインにアクセスしてアプリの動作確認

📸 スクリーンショット:
- ![ALBアクセス](./step6_ecs_fargate_build/step6_alb_access.png)

---

### 3-5. GitHub ActionsでCI/CD構築

- `deploy-ecs.yml` により、自動ビルド＆デプロイを実現
- Push → Build → ECR Push → ECS更新

📘 GitHub Actionsログのスクショは任意

---

### 3-6. CloudWatchによる監視

- CloudWatch Logs:
  - `/ecs/step6-flask-log-group`
- CloudWatch Alarm:
  - `high-cpu-usage-alarm`（CPU > 80%）

📘 GUIのスクショは任意

---

## 4. デプロイ確認

- ALBアクセス後、ブラウザ上に `Hello from Flask inside Docker!` を確認済

📸 スクリーンショット:
- ![最終確認](./step6_ecs_fargate_build/step6_browser_access.png)

---

## ✅ 補足ディレクトリ構成

