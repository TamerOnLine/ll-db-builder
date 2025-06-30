# 🧩 Database Structure – Resume Builder (llol_step09)

This document provides a detailed explanation of the database schema used in the `llol_step09` project, which powers the dynamic and multilingual resume system.

---

## 📚 Main Tables Overview

### 1. `ResumeSection`

Represents a section in the resume (e.g., "Work Experience", "Education", "Skills").

| Field               | Type     | Description                              |
|--------------------|----------|------------------------------------------|
| `id`               | Integer  | Primary key                              |
| `title_translations` | JSON   | Section title in multiple languages      |
| `order`            | Integer  | Display order of the section             |
| `is_visible`       | Boolean  | Whether the section is visible           |
| `paragraphs`       | Relationship | One-to-many with `ResumeParagraph`  |

---

### 2. `ResumeParagraph`

Represents a paragraph inside a section. Can contain multiple fields.

| Field               | Type     | Description                                  |
|--------------------|----------|----------------------------------------------|
| `id`               | Integer  | Primary key                                  |
| `section_id`       | Integer  | Foreign key → `ResumeSection.id`             |
| `order`            | Integer  | Display order within the section             |
| `field_type`       | String   | Type of paragraph (e.g., text, list, etc.)   |
| `is_visible`       | Boolean  | Whether the paragraph is visible             |
| `fields`           | Relationship | One-to-many with `ResumeField`         |

---

### 3. `ResumeField`

Represents an individual entry inside a paragraph (e.g., a job entry, a skill).

| Field               | Type     | Description                                  |
|--------------------|----------|----------------------------------------------|
| `id`               | Integer  | Primary key                                  |
| `paragraph_id`     | Integer  | Foreign key → `ResumeParagraph.id`           |
| `order`            | Integer  | Display order within the paragraph           |
| `title_translations` | JSON   | Field title in multiple languages            |
| `value_translations` | JSON   | Field value in multiple languages            |
| `is_visible`       | Boolean  | Whether the field is visible                 |

---

## 🔗 Relationships Between Tables

```
ResumeSection (1) ──── (∞) ResumeParagraph (1) ──── (∞) ResumeField
```

- Each **`ResumeSection`** can contain multiple **`ResumeParagraph`** entries.
- Each **`ResumeParagraph`** can contain multiple **`ResumeField`** entries.

---

## 🌍 Multilingual Support

All textual fields (`title_translations`, `value_translations`) are stored in JSON format to support dynamic multilingual content rendering.

Example:
```json
{
  "en": "Work Experience",
  "ar": "الخبرات العملية",
  "de": "Berufserfahrung"
}
```

---

## 🎨 Display and Visibility

- Every level (section, paragraph, field) has an `order` and `is_visible` flag.
- This allows for **drag-and-drop reordering** and **conditional rendering** in the UI.

---

## 🛠️ Future Expansion Ideas

| Feature               | Implementation Suggestion                     |
|----------------------|-----------------------------------------------|
| Custom Templates      | Add `ResumeTemplate` table                   |
| Media (images/files) | Extend `ResumeField` with `media_url` column |
| Collaboration        | Add user ownership with `user_id` in sections|

---

## 📌 Summary

The schema is optimized for:
- Flexibility
- Multilingual support
- UI-driven customization
- Scalable resume structuring