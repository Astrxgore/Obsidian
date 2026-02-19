---

kanban-plugin: board

---

## BackLog

- [ ] [[Темплейт]]
	Предмет: #Темплейт
	Дедлайн: @{2025-11-01}
	Тип: #ВУЗ


## This week

- [ ] [[Составить расписание]]
	Предмет: 
	Дедлайн: @{2025-11-30} 
	Тип: #Саморазвитие


## Today

```dataview
table project, due
from "02_ACTION/Tasks"
where status = "next"
sort due asc
```


## In progress



## Done / Review



***

## Archive


%% kanban:settings
```
{"kanban-plugin":"board","list-collapse":[false,false,false,false,false],"show-checkboxes":false,"new-note-folder":"Kanban notes","tag-colors":[],"date-colors":[{"isToday":false,"distance":1,"unit":"days","direction":"after","color":"rgba(255, 0, 226, 1)"},{"distance":3,"unit":"days","direction":"after","color":"rgba(224, 108, 0, 1)"},{"isToday":false,"distance":7,"unit":"days","direction":"after","color":"rgba(183, 199, 0, 1)"},{"isToday":false,"distance":14,"unit":"days","direction":"after","color":"rgba(99, 198, 0, 1)"},{"isToday":false,"distance":1,"unit":"months","direction":"after","color":"rgba(0, 201, 189, 1)"},{"isToday":false,"distance":1,"unit":"months","direction":"before","color":"rgba(255, 0, 0, 1)"},{"isToday":false,"distance":1,"unit":"days","direction":"after"}],"date-picker-week-start":1}
```
%%