# Step2：Terraformによるインフラ自動構築（Infrastructure as Code）

## 1. 概要

本ステップでは、Step1でGUIにより構築したAWSインフラ構成を、  
**Terraformを用いてコードで再現（Infrastructure as Code）**します。

再現性のある構成・変更の容易さ・構成の明確化により、  
「手で作れる」だけではなく「設計通りに再構築できる」エンジニアであることを証明します。

---

## 2. 構成図（Step1）

本ステップのTerraformコードは、以下の構成図に基づいています。  
GUI構築と同様のリソースをコードで再現することを目的とします。

![構成図](./aws_step1_architecture.png)

---

## 3. Terraformディレクトリ構成

