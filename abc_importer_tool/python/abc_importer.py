# ABC Importer Tool for Houdini
# Author: Your Name
# Version: 1.0.0

import hou
import os
from PySide2.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QCheckBox, QLabel, QComboBox, QListWidget, QFileDialog)
from PySide2.QtCore import Qt

class AbcImporterUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 确保窗口总是显示在最前面
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        
        self.folders = []
        self.current_dir = None
        self.options = {
            "Import Without Display": False  # 新的选项，默认为False
        }
        
        self.init_ui()
        self.find_publish_folders()
        
        # 设置窗口大小和位置
        self.resize(400, 600)
        self.center_on_screen()
    
    def center_on_screen(self):
        """将窗口居中显示"""
        desktop = hou.qt.mainWindow().geometry()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)
        
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle('ABC Importer')
        main_layout = QVBoxLayout()
        
        # 文件夹选择部分
        folder_layout = QHBoxLayout()
        folder_label = QLabel('Location:')
        self.folder_combo = QComboBox()
        self.folder_combo.currentIndexChanged.connect(self.on_folder_changed)
        folder_layout.addWidget(folder_label)
        folder_layout.addWidget(self.folder_combo)
        main_layout.addLayout(folder_layout)
        
        # 选项部分
        options_label = QLabel('Import Options:')
        main_layout.addWidget(options_label)
        
        # 添加不显示选项的复选框
        self.option_checkboxes = {}
        checkbox = QCheckBox("Import Without Display")
        checkbox.setChecked(False)  # 默认不勾选
        self.option_checkboxes["Import Without Display"] = checkbox
        main_layout.addWidget(checkbox)
        
        # 文件列表
        self.file_list = QListWidget()
        self.file_list.setSelectionMode(QListWidget.ExtendedSelection)
        main_layout.addWidget(self.file_list)
        
        # 按钮部分
        button_layout = QHBoxLayout()
        self.import_btn = QPushButton('Import Selected')
        self.refresh_btn = QPushButton('Refresh')
        self.import_btn.clicked.connect(self.import_selected)
        self.refresh_btn.clicked.connect(self.refresh_files)
        button_layout.addWidget(self.refresh_btn)
        button_layout.addWidget(self.import_btn)
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
    
    def find_publish_folders(self):
        """查找发布文件夹"""
        hip_path = hou.hipFile.path()
        parent_dir = os.path.dirname(os.path.dirname(hip_path))
        
        self.folders = []
        for folder_name in ['ani', 'mm']:
            publish_path = os.path.join(parent_dir, folder_name, 'publish')
            if os.path.exists(publish_path) and os.path.isdir(publish_path):
                self.folders.append((f'{folder_name.upper()}/publish', publish_path))
                self.folder_combo.addItem(f'{folder_name.upper()}/publish', publish_path)
        
        if self.folders:
            self.current_dir = self.folders[0][1]
            self.refresh_files()
    
    def refresh_files(self):
        """刷新文件列表"""
        self.file_list.clear()
        if not self.current_dir:
            return
            
        for file in os.listdir(self.current_dir):
            if file.endswith('.abc'):
                self.file_list.addItem(file)
    
    def on_folder_changed(self, index):
        """文件夹选择改变时的处理"""
        if index >= 0:
            self.current_dir = self.folder_combo.itemData(index)
            self.refresh_files()
    
    def create_nodes(self):
        """创建节点"""
        obj_context = hou.node("/obj")
        if not obj_context:
            return None, None
            
        geo_node = obj_context.createNode("geo", "alembic_import")
        if not geo_node:
            return None, None
            
        alembic_node = geo_node.createNode("alembic")
        if not alembic_node:
            if geo_node:
                geo_node.destroy()
            return None, None
            
        return geo_node, alembic_node
    
    def setup_node_parameters(self, alembic_node, abc_file):
        """设置节点参数"""
        try:
            file_parm = alembic_node.parm("fileName")
            if not file_parm:
                return False
            file_parm.set(abc_file)
            return True
        except:
            return False
    
    def import_selected(self):
        """导入选中的文件"""
        selected_items = self.file_list.selectedItems()
        if not selected_items:
            return
            
        # 获取是否需要显示
        hide_display = self.option_checkboxes["Import Without Display"].isChecked()
            
        for item in selected_items:
            abc_file = os.path.join(self.current_dir, item.text())
            
            # 创建节点
            geo_node, alembic_node = self.create_nodes()
            if not geo_node or not alembic_node:
                continue
            
            # 设置参数
            if not self.setup_node_parameters(alembic_node, abc_file):
                geo_node.destroy()
                continue
            
            # 完成设置
            geo_node.layoutChildren()
            
            # 根据选项设置显示状态
            if hide_display:
                # 设置几个关键的显示标志
                geo_node.setDisplayFlag(False)
                geo_node.setSelectableInViewport(False)
                alembic_node.setDisplayFlag(False)
                alembic_node.setRenderFlag(False)
                # 确保不会被选中
                geo_node.setCurrent(False)
            else:
                geo_node.setDisplayFlag(True)
                geo_node.setSelectableInViewport(True)
                alembic_node.setDisplayFlag(True)
                alembic_node.setRenderFlag(True)
                geo_node.setCurrent(True, clear_all_selected=True)

def show_importer():
    """显示导入器窗口"""
    # 获取Houdini主窗口作为父窗口
    parent = hou.qt.mainWindow()
    # 创建导入器窗口
    importer = AbcImporterUI(parent)
    importer.show()

if __name__ == "__main__":
    show_importer()
