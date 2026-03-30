### Title: Edit an existing event (partial update with time)

**Preconditions:**
- User is registered
- User is logged into the system
- There is at least one event created and visible on the events page

**Test Steps:**

| Step | Action                                   | Data                                      | Expected Result                                                                 |
|------|---------------------------------------   |-------------------------------------------|---------------------------------------------------------------------------------|
| 1    | Locate the event card on the events page | —                                         | Event card is visible                                                           |
| 2    | Click "Змінити" button on the event card | —                                         | Event edit form opens with current event data pre-filled                        |
| 3    | Update "Тривалість"                      | "3 дні"                                   | Duration is updated from the dropdown                                           |
| 4    | Update "Опис події" field                | "Оновлений короткий опис події"           | Field accepts value (at least 10 characters)                                    |
| 5    | Update "Час початку"                     | "11:00"                                   | Start time is updated                                                           |
| 6    | Update "Час завершення"                  | "14:00"                                   | End time is updated                                                             |
| 7    | Click "Зберегти" button                  | —                                         | Event is successfully updated, only modified fields (duration, description, time) 
|      |                                          |                                           | are changed on the events page                                                  |