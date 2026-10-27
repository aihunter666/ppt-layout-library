---
name: ppt-layout-library
description: 在制作 PPT、PowerPoint 或 HTML 演示时，检索 3207 张详细布局原图，按内容关系、页面类型和横竖比例筛选结构，并比较实际内容预览。
---

# PPT 排版结构原图库

本技能仅收录详细布局的源站原图，共 3207 张。读取 `library/coverage.json` 核对收录数量；自然尺寸以 `library/catalog.json` 为准，原图不保证高清。本库不包含高清实页或固定主题示例图片。

## 检索

打开 `library/index.html` 浏览，或使用 Python 3（无第三方依赖）：

```bash
python3 scripts/search.py --category 流程 --limit 16
python3 scripts/search.py --query 对比 --limit 12
python3 scripts/search.py --group agenda --query 目录
python3 scripts/search.py --aspect 9:16 --category 流程
python3 scripts/search.py --ids MD-B0001 MD-P0005
```

索引保留 MD 编号、别名、来源 ID、分类、关键词、横竖比例及自然尺寸。每张原图位于 `library/assets/MD-编号.png`。只按需检索，不一次输出整个索引。

## 选择与采用

先明确主信息、逻辑关系、要点数、文字长度、图片或数据需求和演示场景，再查看实际图片，核对阅读顺序与内容容量。关系类别命中不等于构图合适，不把检索排名当作适配评分。选型建议见 `library/families.json`，详细说明见 `references/selection.md`。

需要比较时，选取 2–4 个组织方式有实质差异的布局，将同一份实际内容排入候选，沿用当前项目视觉风格。原图不能冒充已试排成稿。字体、色彩、材质和动效由当前项目决定。将采用编号写入故事板或页面规格，通常不放到最终展示页。

本技能提供构图检索和决策支持，不替代故事板、视觉风格或演示文件制作技能。用户指定制作工具时遵循用户要求。

## 资料边界

布局原图供构图参考。不是可编辑模板，不包含可靠的对象坐标、文本容量或内容项数量标签。


仅使用本地原图库，不自动采集或下载其他图片。
