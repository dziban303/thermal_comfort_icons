#!/usr/bin/env python3
import json
import os
from glob import glob
from string import Template
from typing import List, Optional
from xml.dom.minidom import Document, parse

SVG = "svg"
OUTFILE = os.path.join("dist", "thermal_comfort_icons.js")


def get_paths(dom: Document) -> List[str]:
    """Get all path data from the svg file."""
    paths = dom.getElementsByTagName("path")
    path_data = [path.getAttribute("d") for path in paths if path.hasAttribute("d")]
    if not path_data:
        raise ValueError("SVG does not contain any path d attributes")
    return path_data


def get_secondary_path(dom: Document) -> Optional[str]:
    """Get a second path for two-tone icons if available."""
    paths = get_paths(dom)
    if len(paths) == 2:
        return paths[1]
    return None


def get_viewbox(dom: Document) -> Optional[str]:
    """Get the SVG viewBox attribute."""
    svg_node = dom.getElementsByTagName(SVG)[0]
    return svg_node.getAttribute("viewBox") or None


def get_id(dom: Document) -> str:
    """Get the id of the svg file."""
    return dom.getElementsByTagName(SVG)[0].getAttribute("id")


def get_keywords(dom: Document) -> List[str]:
    """Get the keywords of the svg file."""
    desc_tags = dom.getElementsByTagName("desc")
    if len(desc_tags) > 0 and desc_tags[0].firstChild is not None:
        node_value = desc_tags[0].firstChild.nodeValue
        return [keyword for keyword in node_value.split() if keyword]
    return []


doms = [parse(file) for file in glob(os.path.join(SVG, f"*.{SVG}"))]

icons = {}
for dom in doms:
    icon_id = get_id(dom)
    paths = get_paths(dom)
    icon_data = {
        "path": paths[0],
        "keywords": get_keywords(dom),
    }

    viewbox = get_viewbox(dom)
    if viewbox:
        icon_data["viewBox"] = viewbox

    if len(paths) == 2:
        icon_data["secondaryPath"] = paths[1]
    elif len(paths) > 2:
        icon_data["path"] = " ".join(paths)

    icons[icon_id] = icon_data

template = Template(
    """const TC_ICONS_MAP = $icons;

async function getIcon(name) {
  return TC_ICONS_MAP[name];
}

async function getIconList() {
  return Object.entries(TC_ICONS_MAP).map(([icon, content]) => ({
    name: icon,
    keywords: content.keywords,
  }));
}

window.customIcons = window.customIcons || {};
window.customIcons["tc"] = { getIcon, getIconList };

window.customIconsets = window.customIconsets || {};
window.customIconsets["tc"] = getIcon;
"""
)

js = template.substitute(icons=json.dumps(icons, sort_keys=True, indent=2))

with open(OUTFILE, "w") as outfile:
    outfile.write(js)
