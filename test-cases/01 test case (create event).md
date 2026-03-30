### Title: Create a public online event with a required link

**Preconditions:**
- User is registered
- User is logged into the system

**Test Steps:**

| Step | Action                              | Data                                      | Expected Result                                                                 |
|------|-------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------|
| 1    | Click "Створити подію" button       | —                                         | Event creation form is opened                                                   |
| 2    | Fill in "Заголовок" field           | "Моя подія"                               | Field accepts the entered value                                                 |
| 3    | Select "Тривалість"                 | "2 години"                                | Duration is selected from the dropdown                                         |
| 4    | Select "Тематика події"             | "Економічний"                             | Category is selected                                                            |
| 5    | Select "Тип події"                  | "Відкрита"                                | Event type is set                                                               |
| 6    | Select "Формат події"               | "Онлайн"                                  | "Посилання на подію" field is displayed                                         |
| 7    | Fill in "Посилання на подію" field  | "https://meet.example.com/event"          | Field accepts a valid link                                                      |
| 8    | Fill in "Опис події" field          | "Це тестовий опис події"                  | Field accepts value (at least 10 characters)                                    |
| 9    | Select "Дата події"                 | "2026-04-01"                              | Date is set                                                                     |
| 10   | Select "Час початку"                | "10:00"                                   | Start time is set                                                               |
| 11   | Select "Час завершення"             | "12:00"                                   | End time is set                                                                 |
| 12   | Click "Публікувати" button          | —                                         | Event is successfully created and its card appears on the events page           |