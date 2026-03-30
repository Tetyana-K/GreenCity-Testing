### Title: Add a comment to an event

**Preconditions:**
- User is registered
- User is logged into the system
- There is at least one event created and visible on the events page

**Test Steps:**

| Step | Action                                      | Data                                 | Expected Result                                                       |
|------|--------------------------------------       |--------------------------------------|-----------------------------------------------------------------------|
| 1    | Locate the event card on the events page    | —                                    | Event card is visible                                                 |
| 2    | Click "Детальніше" button on the event card | —                                    | Detailed event window opens                                           |
| 3    | Fill in "Коментарі" field                   | "Це тестовий коментар"               | Field accepts the entered text                                        |
| 4    | Click on "Коментувати" button               | —                                    | Comment is submitted                                                  |
| 5    | Verify the comment appears in the comments list | —                                | The new comment is displayed in the comments list with correct content|