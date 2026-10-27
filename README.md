# PPT Layout Library

3207 张布局原图，以及对应的本地检索脚本和离线浏览页面。

## 在线浏览

**访问布局库：[https://aihunter666.github.io/ppt-layout-library/](https://aihunter666.github.io/ppt-layout-library/)**

打开链接即可搜索、筛选和查看全部布局，无需下载或安装。

## 直接浏览

1. 下载完整仓库（Code → Download ZIP），并解压。
2. 双击仓库根目录的 `index.html`，即可浏览整个布局库。
3. 按关键词、编号、页面类型、横竖比例和分类筛选；点击卡片查看图片。

**无需安装 Python，无需启动 HTTP 服务，也无需联网。** 请保留解压后的目录结构，不要只单独复制 HTML 文件。也可以直接打开 `library/index.html`。

浏览页面采用普通本地 JavaScript 和相对图片路径，不使用 `fetch`、ES Module、CDN 或网络字体。

## 命令行检索（可选）

```bash
python3 scripts/search.py --query 流程 --limit 12
python3 scripts/search.py --group professional --category 对比
python3 scripts/search.py --aspect 9:16
python3 scripts/search.py --ids MD-C0001
```

命令行检索需要 Python 3，无第三方依赖；HTML 浏览不需要 Python。检索结果包含本地图片路径、编号、别名、分类、自然尺寸和 SHA256。

## 作为技能使用

仓库根目录包含 `SKILL.md`，可作为 `ppt-layout-library` 技能目录使用。按内容关系选择布局，查看实际图片，再用当前项目的内容和视觉风格制作页面。

## 数据范围

现已收录 **3207 张布局原图**。
