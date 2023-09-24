import xml.etree.ElementTree as ET
from sklearn.model_selection import KFold

# Load XML data from file
tree = ET.parse("D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai4/spam.xml")
root = tree.getroot()

# Define the number of folds for cross-validation
num_folds = 5
kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)

def prune_tree(node):
    if node.tag.startswith("Node"):
        # Recursively process child nodes
        for child in node:
            prune_tree(child)
        
        # Prune node if it's a leaf with few samples
        if len(node.attrib) > 0 and int(node.attrib['items']) < 10:
            parent = node.getparent()
            if parent is not None:
                parent.remove(node)

# Perform cross-validation
fold = 1
for train_idx, test_idx in kf.split(root):
    train_root = root.copy()
    test_root = root.copy()
    
    # Prune the training tree
    prune_tree(train_root)
    
    # Create a new ElementTree from the pruned training root
    pruned_train_tree = ET.ElementTree(train_root)
    
    # Save the pruned training tree to a new XML file
    pruned_train_tree.write(f"D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai4/train_fold_{fold}.xml", encoding="utf-8", xml_declaration=True)
    
    # Save the testing tree to a new XML file
    pruned_test_tree = ET.ElementTree(test_root)
    pruned_test_tree.write(f"D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai4/test_fold_{fold}.xml", encoding="utf-8", xml_declaration=True)
    
    fold += 1
