from main.extensions import db

from .resume_section import ResumeSection
from .resume_paragraph import ResumeParagraph
from .resume_field import ResumeField
from .resume_setting import Setting
from .Section import Section
from .LanguageOption import LanguageOption
from .NavigationLink import NavigationLink
from .sidebar_link import SidebarLink  # تأكد من استيراد SidebarLink إذا كان موجودًا


# تأكد من استيراد db فقط إذا كان ذلك منطقيًا في السياق
# من مكان تعريف db:
# from main import db

__all__ = [
    "ResumeSection",
    "ResumeParagraph",
    "ResumeField",
    "Setting",
    "Section",
    "LanguageOption",
    "NavigationLink",
    "SidebarLink"
]
