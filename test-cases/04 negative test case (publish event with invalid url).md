### Title: Negative test – Publish online event with invalid link

**Preconditions:**
- User is registered
- User is logged into the system
- User is on the "Створення події" form

**Test Steps:**

| Step | Action                              | Data                                      | Expected Result                                                                 |
|------|-------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------|
| 1    | Fill in "Заголовок події" field     | "Тестова онлайн подія"                     | Field accepts the entered value                                                 |
| 2    | Select "Тривалість"                 | "2 дні"                                   | Duration is selected from the dropdown                                          |
| 3    | Select "Тип події"                  | "Відкрита"                                | Event type is set                                                               |
| 4    | Select "Тематика події"             | "Екологічний"                             | Category is selected                                                            |
| 5    | Select "Формат події"               | "Онлайн"                                  | "Посилання на подію" field is displayed                                         |
| 6    | Fill in "Посилання на подію" field  | "meet.example.com/event"                  | Field accepts input, but it is invalid (does not start with http:// or https://) |
| 7    | Fill in "Опис події" field          | "Тестовий опис онлайн події"              | Field accepts value (at least 10 characters)                                     |
| 8    | Select "Дата події"                 | "2026-04-05"                              | Date is set                                                                     |
| 9    | Select "Час початку"                | "10:00"                                   | Start time is set                                                               |
| 10   | Select "Час завершення"             | "12:00"                                   | End time is set                                                                 |
| 11   | Click "Публікувати" button          | —                                         | Event is **not published**, system displays validation error: "Посилання має починатися з http:// або https://" |