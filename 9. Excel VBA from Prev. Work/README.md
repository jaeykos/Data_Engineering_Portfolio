### 1. SAFE Column Rundown
   - SAFE is a building floor analysis software and it calculates the weight transferred from to slab to column
   - One SAFE model consists of one floor; for a building with multiple floors, user needs to create a model for each floor
   - SAFE includes API, which allows user to extract the weight each column is supporting
   - My spreadsheet extracts the weight on column from each floor model, and calculates the cumulative  weight of lower columns

### 2. SAP2000 Multiple Seciton Cutter
   - SAP2000 is commonly used structural engineering software that analyses mechanical behaviour of structure (eg. how building moves under weight)
   - It includes a feature called 'section', which allows user to slice a model to observe its internal forces
   - SAFE includes API, which allows user to extract internal forces of a section
   - My spreadsheet automates creation of multiple sections in SAP2000 and extraction of their internal forces, as well creation internal force diagrams
