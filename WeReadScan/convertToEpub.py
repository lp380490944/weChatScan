from ebooklib import epub

# 指定HTML文件的路径
html_file_path = '吴医生陪你科学孕产.html'

# 重新读取HTML内容
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# 创建一个新的EPUB书籍对象
book = epub.EpubBook()

# 设置书籍的基本信息
book.set_identifier('id123456')
book.set_title('吴医生陪你科学孕产')
book.set_language('zh')

# 创建书籍的主要内容
c1 = epub.EpubHtml(title='内容', file_name='content.xhtml', lang='zh')
c1.content = html_content

# 将内容添加到书籍中
book.add_item(c1)

# 定义目录结构
book.toc = (c1,)

# 定义书籍的spine结构
book.spine = ['nav', c1]

# 将书籍保存为EPUB文件
epub.write_epub('.', book)
