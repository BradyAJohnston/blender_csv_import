# blender_csv_import

A simple and fast CSV file importer.

Download here: https://extensions.blender.org/add-ons/csv-importer/

Walkthrough video:



https://github.com/user-attachments/assets/1b8a26d7-ce35-4717-bf73-bc05dbf3912a





## How to Use

Option 1: Drag and drop your CSV file directly into Blender’s viewport.

Option 2: Use the menu:
File → Import → CSV

### **Using the Data**  
- The imported data will appear in Blender’s **Spreadsheet Editor**.  
- Use the **Named Attribute** in **Geometry Nodes** to access the imported data.


And the data will show up in the speadsheet:

<img width="900" alt="image" src="https://github.com/user-attachments/assets/36f7e277-ab73-4335-936c-9ca25a32683b" />



you can reproduce the above example with this geometry nodes setup.
The corresponding Blender file can be downloaded [here](https://github.com/kolibril13/blender_csv_import/blob/main/generate_data/example_file_california_bounding_box.blend)

<img width="1471" alt="image" src="https://github.com/user-attachments/assets/515e7727-e995-4672-918a-1234c9fd0ad7" />




## Support this project 
   [![Buy Me a Coffee](https://img.shields.io/static/v1?label=&message=Buy%20Me%20a%20Coffee&color=FFDD00&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jan_hendrik)

## Development instructions

1. Install https://github.com/JacquesLucke/blender_vscode
2. Enable the setting "Blender › Addon: Reload On Save"
3. Command+Shift+P -> Blender: Build and Start
4. Start coding with __init__.py

### Build the extension:

For downloading the wheels files, run: 
```
/Applications/Blender.app/Contents/MacOS/Blender -b -P build.py
```
For building the app for all platforms, run
```
/Applications/Blender.app/Contents/MacOS/Blender --command extension build --split-platforms
```

### Run tests:

```
uv sync --all-extras --dev
uv run -m pytest
```

# Changelog

## Version 0.1.5

### New Features
- **Drag-and-Drop:** Added support for drag-and-drop functionality into windows other than the viewport.
- **API Import Call:** Introduced an API for importing CSV data (note: this feature is not yet stable and may change in the future). Usage examples:

```python
from csv_importer.csv import load_csv
from csv_importer.parsers import polars_df_to_bob
```

### Usage Examples

1. **Loading CSV File:**
   ```python
   >>> from csv_importer.csv import load_csv
   >>> bob = load_csv("/Users/jan-hendrik/Desktop/data_california_housing.csv")
   >>> bob
   bpy.data.objects['CSV_data_california_housing']
   ```

2. **Converting Polars DataFrame:**
   ```python
   from io import StringIO
   import polars as pl
   from csv_importer.parsers import polars_df_to_bob

   csv_data = StringIO(
   """FloatVal,IntVal,BoolVal,StringVal
   1.23,10,true,Hello
   4.56,20,false,World"""
   )
   df = pl.read_csv(csv_data)
   bob = polars_df_to_bob(df, name="Test")
   ```

---

### Blender Version Support
- **Supported Versions:**
  - Blender 4.3.1 and later.
  - Blender 4.2.5 (requires testing, I did not try this yet).
- **Known Issue (Resolved):**
  - A bug in earlier Blender versions ([issue link](https://github.com/kolibril13/blender_csv_import/issues/1#issuecomment-2556517316)) has been fixed.

---

### Improvements
- Properly skip string data when processing CSVs.
- Added test coverage for the CSV importer.
- Refactored the project structure for better organization.

---

### Additional Updates
- Use a new data wrapper using [databpy](https://github.com/BradyAJohnston/databpy) by @BradyAJohnston.
- Update to latest Polars library version: [1.19.0](https://pypi.org/project/polars/1.19.0/).
  
## 0.1.4

* Rename the imported mesh from "ImportedMesh" to "CSV_filename"




<!-- # might be a useful import snippet

import polars as pl
import bpy
from bl_ext.blender_org.csv_importer import PolarsMesh -->

<!-- 
and here another one
```

import polars as pl
import bpy
from bl_ext.blender_org.csv_importer import PolarsMesh

df = pl.read_json("/Users/jan-hendrik/projects/blender_csv_import/generate_data/dino_star_vectors.json")
# Explode the columns to transform list[list] into individual rows
df = df.explode(["Dino", "Star"])



blender_mesh = PolarsMesh(dataframe=df, object_name=f"JSON OBJ")

# Link the new mesh to the Blender scene
bpy.context.collection.objects.link(blender_mesh.point_obj)

``` -->