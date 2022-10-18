### 1. SAFE Column Rundown
   - SAFE is a concrete slab analysis software. It also calculates the weight transferred from to slab to column
   - One SAFE model consists of one floor of slab; for a building with multiple floors, user needes to create multiple models for each floor
   - SAFE includes API, which allows user to extract weight each column is supporting
   - My spreadsheet extracts weight on column from each floor model, and calculates cumulative supporting weight of lower columns

### 2. SAP2000 Multiple Seciton Cutter
   - SAP2000 is commonly used structural engineering software that analyses mechanical behaviour of structure (eg. how building moves under weight)
   - It includes a feature called 'section', which allows user to slice a structure model to observe the internal forces
   - SAFE includes API, which allows user to extract internal force of a section
   - My spreadsheet automates creation of multiple sections in SAP2000 and extracts internal forces, as well create force diagrams
   

