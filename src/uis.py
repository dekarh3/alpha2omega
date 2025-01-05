dlg_ui = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>dlg</class>
 <widget class="QWidget" name="dlg">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>445</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QTableView" name="view_primary"/>
   </item>
   <item>
    <widget class="QPushButton" name="button_add_row">
     <property name="text">
      <string>Add a row</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="button_del_row">
     <property name="text">
      <string>Delete a row</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="button_done">
     <property name="text">
      <string>Done</string>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
widget_main_window_ui = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>widget_main_window</class>
 <widget class="QWidget" name="widget_main_window">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>461</width>
    <height>789</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QFrame" name="frame">
     <property name="frameShape">
      <enum>QFrame::StyledPanel</enum>
     </property>
     <property name="frameShadow">
      <enum>QFrame::Raised</enum>
     </property>
     <layout class="QVBoxLayout" name="verticalLayout_2">
      <item>
       <widget class="QPushButton" name="button_magic">
        <property name="sizePolicy">
         <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <property name="text">
         <string>Press HERE for the MAGIC</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="button_exit">
        <property name="sizePolicy">
         <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <property name="text">
         <string>Press HERE to EXIT</string>
        </property>
       </widget>
      </item>
     </layout>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
ThemeTable_ui = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>dlg</class>
 <widget class="QWidget" name="dlg">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>445</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QTableView" name="view_primary"/>
   </item>
   <item>
    <widget class="QPushButton" name="button_add_row">
     <property name="text">
      <string>Add a row</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="button_del_row">
     <property name="text">
      <string>Delete a row</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="button_done">
     <property name="text">
      <string>Done</string>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
