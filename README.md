### About
This is a plugin for TiddlyWeb to enforce a data model

### URI
/bags/{bag_name}/tiddlers/_model
/bags/model/tiddlers/{bag_name}

### JSON

```JSON
{
   "attributeTypes": [
      { "name": 'name', "mandatory": true,  "immutable": true},
      { "name": 'description', "mandatory": true},
      { "name": 'URL'},
   ],
   "associationTypes": [
      { "cardinallity": '1-*', "name": 'Links', "to_bag": 'links' } 
   ]
}
```
