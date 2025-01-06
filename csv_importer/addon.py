import bpy
from .ops import ImportCsvPolarsOperator, CSV_FH_import


# Register the operator and menu entry
def menu_func_import(self, context):
    self.layout.operator(ImportCsvPolarsOperator.bl_idname, text="CSV 🐻 (.csv)")


def register():
    bpy.utils.register_class(ImportCsvPolarsOperator)
    bpy.utils.register_class(CSV_FH_import)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.utils.unregister_class(CSV_FH_import)
    bpy.utils.unregister_class(ImportCsvPolarsOperator)