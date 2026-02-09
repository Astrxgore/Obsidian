<%*
// Путь к папке с ежедневными заметками
const folderPath = "Daily"; 

// Получаем все файлы в папке
const dailyFiles = app.vault.getFiles().filter(f => f.path.startsWith(folderPath + "/"));

// Сортировка по имени файла (по дате, если имена датой)
dailyFiles.sort((a, b) => a.basename.localeCompare(b.basename));

// Формируем Markdown список ссылок
let mdLinks = "";
for (let file of dailyFiles) {
    mdLinks += `- [[${file.basename}]]\n`;
}

tR += mdLinks;
%>