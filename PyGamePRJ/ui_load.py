template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>635</width>
    <height>495</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string/>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="styleSheet">
    <string notr="true"/>
   </property>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>631</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="frameShape">
     <enum>QFrame::NoFrame</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <property name="text">
     <string>&quot;НУ, ПОГОДИ!&quot;</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="less1_btn">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>170</y>
      <width>121</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>10</pointsize>
      <weight>50</weight>
      <italic>true</italic>
      <bold>false</bold>
      <underline>false</underline>
      <strikeout>false</strikeout>
      <kerning>true</kerning>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="mouseTracking">
     <bool>false</bool>
    </property>
    <property name="tabletTracking">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhNone</set>
    </property>
    <property name="text">
     <string>Урок 1</string>
    </property>
    <property name="flat">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QPushButton" name="play_btn">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>160</y>
      <width>121</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhNone</set>
    </property>
    <property name="text">
     <string>Начать</string>
    </property>
    <property name="autoRepeat">
     <bool>false</bool>
    </property>
    <property name="autoExclusive">
     <bool>false</bool>
    </property>
    <property name="autoDefault">
     <bool>false</bool>
    </property>
    <property name="default">
     <bool>false</bool>
    </property>
    <property name="flat">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>100</y>
      <width>211</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="frameShape">
     <enum>QFrame::NoFrame</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <property name="text">
     <string>Обучение</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="wordWrap">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>100</y>
      <width>201</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="frameShape">
     <enum>QFrame::NoFrame</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <property name="lineWidth">
     <number>0</number>
    </property>
    <property name="text">
     <string>Игра</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="wordWrap">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>430</x>
      <y>100</y>
      <width>211</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="frameShape">
     <enum>QFrame::NoFrame</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <property name="text">
     <string>На рекорд</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="wordWrap">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QPushButton" name="less2_btn">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>250</y>
      <width>121</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>10</pointsize>
      <weight>50</weight>
      <italic>true</italic>
      <bold>false</bold>
      <underline>false</underline>
      <strikeout>false</strikeout>
      <kerning>true</kerning>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhNone</set>
    </property>
    <property name="text">
     <string>Урок 2</string>
    </property>
   </widget>
   <widget class="QPushButton" name="ach_btn">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>239</y>
      <width>121</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhNone</set>
    </property>
    <property name="text">
     <string>Достижения</string>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>crown.png</normaloff>crown.png</iconset>
    </property>
    <property name="flat">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QPushButton" name="less3_btn">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>330</y>
      <width>121</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>10</pointsize>
      <weight>50</weight>
      <italic>true</italic>
      <bold>false</bold>
      <underline>false</underline>
      <strikeout>false</strikeout>
      <kerning>true</kerning>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="mouseTracking">
     <bool>false</bool>
    </property>
    <property name="focusPolicy">
     <enum>Qt::NoFocus</enum>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);
</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhNone</set>
    </property>
    <property name="text">
     <string>Урок 3</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_8">
    <property name="geometry">
     <rect>
      <x>570</x>
      <y>440</y>
      <width>40</width>
      <height>40</height>
     </rect>
    </property>
    <property name="text">
     <string notr="true"/>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>png-transparent-computer-icons-setting-icon-cdr-svg-setting-icon.png</normaloff>png-transparent-computer-icons-setting-icon-cdr-svg-setting-icon.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>25</width>
      <height>25</height>
     </size>
    </property>
    <property name="shortcut">
     <string notr="true"/>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>300</y>
      <width>161</width>
      <height>91</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="frameShape">
     <enum>QFrame::HLine</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Sunken</enum>
    </property>
    <property name="text">
     <string>Ваш рекорд:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignHCenter|Qt::AlignTop</set>
    </property>
   </widget>
   <widget class="QLCDNumber" name="record_lcd">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>360</y>
      <width>161</width>
      <height>41</height>
     </rect>
    </property>
    <property name="lineWidth">
     <number>1</number>
    </property>
    <property name="midLineWidth">
     <number>0</number>
    </property>
    <property name="smallDecimalPoint">
     <bool>false</bool>
    </property>
    <property name="digitCount">
     <number>8</number>
    </property>
    <property name="mode">
     <enum>QLCDNumber::Dec</enum>
    </property>
    <property name="value" stdset="0">
     <double>0.000000000000000</double>
    </property>
   </widget>
   <widget class="Line" name="line">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>160</y>
      <width>3</width>
      <height>320</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_2">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>160</y>
      <width>3</width>
      <height>320</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_3">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>160</y>
      <width>3</width>
      <height>320</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_4">
    <property name="geometry">
     <rect>
      <x>1</x>
      <y>150</y>
      <width>640</width>
      <height>3</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>320</y>
      <width>161</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>image021-6.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>240</y>
      <width>161</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>image021-6.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_10">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>160</y>
      <width>161</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>image021-6.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_13">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>160</y>
      <width>121</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>image021-6.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_15">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>410</y>
      <width>161</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>image021-6.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_14">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>220</y>
      <width>121</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>image021-6.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_16">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>280</y>
      <width>121</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>image021-6.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_17">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>340</y>
      <width>121</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>image021-6.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QPushButton" name="lvl1_btn">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>170</y>
      <width>101</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>10</pointsize>
      <weight>50</weight>
      <italic>true</italic>
      <bold>false</bold>
      <underline>false</underline>
      <strikeout>false</strikeout>
      <kerning>true</kerning>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhNone</set>
    </property>
    <property name="text">
     <string>Уровень 1</string>
    </property>
   </widget>
   <widget class="QPushButton" name="lvl2_btn">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>230</y>
      <width>101</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>10</pointsize>
      <weight>50</weight>
      <italic>true</italic>
      <bold>false</bold>
      <underline>false</underline>
      <strikeout>false</strikeout>
      <kerning>true</kerning>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhNone</set>
    </property>
    <property name="text">
     <string>Уровень 2</string>
    </property>
   </widget>
   <widget class="QPushButton" name="lvl3_btn">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>290</y>
      <width>101</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>10</pointsize>
      <weight>50</weight>
      <italic>true</italic>
      <bold>false</bold>
      <underline>false</underline>
      <strikeout>false</strikeout>
      <kerning>true</kerning>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhNone</set>
    </property>
    <property name="text">
     <string>Уровень 3</string>
    </property>
   </widget>
   <widget class="QPushButton" name="lvl4_btn">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>350</y>
      <width>101</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>10</pointsize>
      <weight>50</weight>
      <italic>true</italic>
      <bold>false</bold>
      <underline>false</underline>
      <strikeout>false</strikeout>
      <kerning>true</kerning>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhNone</set>
    </property>
    <property name="text">
     <string>Уровень 4</string>
    </property>
   </widget>
   <widget class="QPushButton" name="lvl5_btn">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>420</y>
      <width>121</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Comic Sans MS</family>
      <pointsize>10</pointsize>
      <weight>50</weight>
      <bold>false</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhNone</set>
    </property>
    <property name="text">
     <string>Финал</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>71</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>Screenshot_1.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_19">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>230</y>
      <width>161</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>image021-6.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_18">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>150</y>
      <width>161</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 0);</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>image021-6.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>-1090</x>
      <y>-320</y>
      <width>1801</width>
      <height>951</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>фон.jpg</pixmap>
    </property>
   </widget>
   <zorder>label_7</zorder>
   <zorder>label_18</zorder>
   <zorder>label_19</zorder>
   <zorder>label_9</zorder>
   <zorder>label_10</zorder>
   <zorder>label_8</zorder>
   <zorder>label</zorder>
   <zorder>less1_btn</zorder>
   <zorder>play_btn</zorder>
   <zorder>label_2</zorder>
   <zorder>label_3</zorder>
   <zorder>label_4</zorder>
   <zorder>less2_btn</zorder>
   <zorder>ach_btn</zorder>
   <zorder>less3_btn</zorder>
   <zorder>pushButton_8</zorder>
   <zorder>label_5</zorder>
   <zorder>record_lcd</zorder>
   <zorder>line</zorder>
   <zorder>line_2</zorder>
   <zorder>line_3</zorder>
   <zorder>line_4</zorder>
   <zorder>label_13</zorder>
   <zorder>label_15</zorder>
   <zorder>label_14</zorder>
   <zorder>label_16</zorder>
   <zorder>label_17</zorder>
   <zorder>lvl1_btn</zorder>
   <zorder>lvl2_btn</zorder>
   <zorder>lvl3_btn</zorder>
   <zorder>lvl4_btn</zorder>
   <zorder>lvl5_btn</zorder>
   <zorder>label_6</zorder>
  </widget>
 </widget>
 <tabstops>
  <tabstop>less1_btn</tabstop>
  <tabstop>less2_btn</tabstop>
  <tabstop>less3_btn</tabstop>
  <tabstop>play_btn</tabstop>
  <tabstop>ach_btn</tabstop>
  <tabstop>pushButton_8</tabstop>
 </tabstops>
 <resources>
  <include location="123.qrc"/>
 </resources>
 <connections/>
</ui>
'''
