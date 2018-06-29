
# Ventura
A Simple xml-based updater in python 3.6 with no try-catch statement, use carefully.

Created as substitute of [updatewp]({{site.url}}/{{site.baseurl}}p/rb-scripts/updatewp) in a series of post to a forum.

## Usage

### Installation

First you need to install the package using ``pip install ventura`` and import in your project with ``import ventura``.

### Documentation

**update_if_is_need** *>> version (double), xml_url (string), path = "" (string, optional)*
version: *current project version*
xml_url: *url of the xml file on web*
path: *path where the new version will be downloaded and unpacked*

### XML format

```xml:
<?xml version="1.0" encoding="UTF-8"?>  
<ventura>  
	<update version="0.1">  
		<url>https://um.link</url>  
		<delete>file_to_delete1.txt,folder1\</delete>  
	</update>  
</ventura>
```
ventura: *root node*
update: *nodes with update information, you can have various of it. Version attribute says wich version is it.*
url: *file to download url, only one by node. Must be inside of a update node.*
delete: *files and folders to delete of previous version separated by commas, put a backslash "\" if is a folder. Must be inside of a update node and only one by node.*
