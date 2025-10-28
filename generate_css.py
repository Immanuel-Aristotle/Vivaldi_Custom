import yaml

template = """
/* === Auto generated CSS for Vivaldi Bookmark Folders === */
{rules}
"""

rule_block = """
/* Folder {id} */
.bookmark-bar button.folder[data-id="{id}"] svg {{
  display: none !important;
}}

.bookmark-bar button.folder[data-id="{id}"]::before {{
  content: "";
  display: inline-block;
  width: 18px;
  height: 18px;
  background-image: url("{url}");
  background-size: contain;
  background-repeat: no-repeat;
  margin-right: 4px;
  vertical-align: middle;
}}
"""

with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

rules = ""
for folder_id, url in config.items():
    rules += rule_block.format(id=folder_id, url=url)

with open("custom.css", "w") as f:
    f.write(template.format(rules=rules))

print("✅ Generated custom.css successfully!")
