import os

# 所有需要创建的文件（完整覆盖你的 nav）
files = [
    "docs/ai/index.md",

    "docs/ai/math/index.md",
    "docs/ai/math/linear_algebra/index.md",
    "docs/ai/math/linear_algebra/vector.md",
    "docs/ai/math/linear_algebra/matrix.md",
    "docs/ai/math/linear_algebra/eigenvalue.md",
    "docs/ai/math/calculus/index.md",
    "docs/ai/math/calculus/derivative.md",
    "docs/ai/math/calculus/chain_rule.md",
    "docs/ai/math/probability_statistics.md",
    "docs/ai/math/information_theory.md",

    "docs/ai/deep_learning/index.md",
    "docs/ai/deep_learning/neural_network/index.md",
    "docs/ai/deep_learning/neural_network/forward.md",
    "docs/ai/deep_learning/neural_network/backward.md",
    "docs/ai/deep_learning/neural_network/loss.md",
    "docs/ai/deep_learning/neural_network/activation.md",
    "docs/ai/deep_learning/neural_network/linear.md",
    "docs/ai/deep_learning/cnn/index.md",
    "docs/ai/deep_learning/cnn/yolo.md",
    "docs/ai/deep_learning/rnn.md",
    "docs/ai/deep_learning/transformer.md",
    "docs/ai/deep_learning/gpt.md",

    "docs/ai/transformer_llm/index.md",
    "docs/ai/transformer_llm/attention.md",
    "docs/ai/transformer_llm/mask.md",
    "docs/ai/transformer_llm/kv_cache.md",
    "docs/ai/transformer_llm/rope.md",
    "docs/ai/transformer_llm/gpt_architecture.md",
    "docs/ai/transformer_llm/inference.md",
    "docs/ai/transformer_llm/tokenization.md",

    "docs/ai/data/index.md",
    "docs/ai/data/datasets/index.md",
    "docs/ai/data/datasets/lccc.md",
    "docs/ai/data/datasets/wechat_chat.md",
    "docs/ai/data/datasets/apple_health.md",
    "docs/ai/data/cleaning.md",
    "docs/ai/data/collection/index.md",
    "docs/ai/data/collection/requests.md",
    "docs/ai/data/storage.md",

    "docs/ai/training/index.md",
    "docs/ai/training/batch.md",
    "docs/ai/training/learning_rate.md",
    "docs/ai/training/residual_network.md",
    "docs/ai/training/vanishing_gradient.md",

    "docs/ai/reinforcement_learning/index.md",
    "docs/ai/optimization/index.md",

    "docs/ai/frameworks/index.md",
    "docs/ai/frameworks/numpy.md",
    "docs/ai/frameworks/pytorch.md",
    "docs/ai/frameworks/huggingface.md",
    "docs/ai/frameworks/datasets.md",

    "docs/ai/industry/index.md",
]

# 默认内容
def generate_content(path):
    title = os.path.splitext(os.path.basename(path))[0]

    if title == "index":
        title = os.path.basename(os.path.dirname(path)) or "AI学习"

    return f"""# {title}

🚧 正在更新中...

---

## 📌 计划内容

- （待补充）
"""

# 创建文件
for file in files:
    os.makedirs(os.path.dirname(file), exist_ok=True)

    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:
            f.write(generate_content(file))

print("✅ 所有目录 + md 文件已生成完成！")