<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>InterfazViva</class>
 <widget class="QDialog" name="InterfazViva">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1102</width>
    <height>853</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QTabWidget" name="Vistas">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1101</width>
     <height>851</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>20</pointsize>
    </font>
   </property>
   <property name="currentIndex">
    <number>2</number>
   </property>
   <widget class="QWidget" name="Inicio">
    <attribute name="title">
     <string>Inicio</string>
    </attribute>
    <widget class="QTextBrowser" name="textBrowser">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>20</y>
       <width>931</width>
       <height>111</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Modern</family>
      </font>
     </property>
     <property name="html">
      <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Modern'; font-size:20pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p align=&quot;center&quot; style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:'MS Shell Dlg 2'; font-size:48pt;&quot;&gt;Residencia VivAlma&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
     </property>
    </widget>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>250</x>
       <y>420</y>
       <width>55</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPlainTextEdit" name="EntradaUsuario">
     <property name="geometry">
      <rect>
       <x>160</x>
       <y>280</y>
       <width>731</width>
       <height>61</height>
      </rect>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit">
     <property name="geometry">
      <rect>
       <x>160</x>
       <y>220</y>
       <width>141</width>
       <height>61</height>
      </rect>
     </property>
     <property name="text">
      <string>Usuario:</string>
     </property>
    </widget>
    <widget class="QPlainTextEdit" name="EntradaContra">
     <property name="geometry">
      <rect>
       <x>160</x>
       <y>420</y>
       <width>731</width>
       <height>61</height>
      </rect>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_2">
     <property name="geometry">
      <rect>
       <x>160</x>
       <y>360</y>
       <width>271</width>
       <height>61</height>
      </rect>
     </property>
     <property name="text">
      <string>Password:</string>
     </property>
    </widget>
    <widget class="QPushButton" name="IniciarSesion">
     <property name="geometry">
      <rect>
       <x>380</x>
       <y>500</y>
       <width>311</width>
       <height>61</height>
      </rect>
     </property>
     <property name="text">
      <string>Iniciar Sesión</string>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="Horarios">
    <attribute name="title">
     <string>Horario del día</string>
    </attribute>
    <widget class="QTableView" name="TablaHorarios">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>130</y>
       <width>621</width>
       <height>631</height>
      </rect>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_6">
     <property name="geometry">
      <rect>
       <x>700</x>
       <y>260</y>
       <width>221</width>
       <height>51</height>
      </rect>
     </property>
     <property name="text">
      <string>Hora:</string>
     </property>
    </widget>
    <widget class="QComboBox" name="NombresPacientes">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>30</y>
       <width>621</width>
       <height>71</height>
      </rect>
     </property>
     <item>
      <property name="text">
       <string>Omar Perez</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Ricardo Flores</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Jacobo Sanchez</string>
      </property>
     </item>
    </widget>
    <widget class="QPushButton" name="GuardarHoras">
     <property name="geometry">
      <rect>
       <x>730</x>
       <y>610</y>
       <width>251</width>
       <height>81</height>
      </rect>
     </property>
     <property name="text">
      <string>GUARDAR</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_7">
     <property name="geometry">
      <rect>
       <x>700</x>
       <y>420</y>
       <width>221</width>
       <height>51</height>
      </rect>
     </property>
     <property name="text">
      <string>Minutos:</string>
     </property>
    </widget>
    <widget class="QComboBox" name="HorasComoBox">
     <property name="geometry">
      <rect>
       <x>700</x>
       <y>310</y>
       <width>381</width>
       <height>61</height>
      </rect>
     </property>
     <item>
      <property name="text">
       <string>00</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>01</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>02</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>03</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>04</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>05</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>06</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>07</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>08</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>09</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>10</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>11</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>12</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>13</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>14</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>15</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>16</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>17</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>18</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>19</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>20</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>21</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>22</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>23</string>
      </property>
     </item>
    </widget>
    <widget class="QComboBox" name="MinutosComoBox">
     <property name="geometry">
      <rect>
       <x>700</x>
       <y>470</y>
       <width>381</width>
       <height>61</height>
      </rect>
     </property>
     <item>
      <property name="text">
       <string>00</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>01</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>02</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>03</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>04</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>05</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>06</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>07</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>08</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>09</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>10</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>11</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>12</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>13</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>14</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>15</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>16</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>17</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>18</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>19</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>20</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>21</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>22</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>23</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>24</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>25</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>26</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>27</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>28</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>29</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>30</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>31</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>32</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>33</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>34</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>35</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>36</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>37</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>38</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>39</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>40</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>41</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>42</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>43</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>44</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>45</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>46</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>47</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>48</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>49</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>50</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>51</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>52</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>53</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>54</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>55</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>56</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>57</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>58</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>59</string>
      </property>
     </item>
    </widget>
   </widget>
   <widget class="QWidget" name="SignosVitales">
    <attribute name="title">
     <string>Signos Vitales</string>
    </attribute>
    <widget class="QTableView" name="TablaSignosVitales">
     <property name="geometry">
      <rect>
       <x>50</x>
       <y>110</y>
       <width>561</width>
       <height>611</height>
      </rect>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_3">
     <property name="geometry">
      <rect>
       <x>680</x>
       <y>110</y>
       <width>221</width>
       <height>51</height>
      </rect>
     </property>
     <property name="text">
      <string>Temperatura:</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_4">
     <property name="geometry">
      <rect>
       <x>680</x>
       <y>270</y>
       <width>221</width>
       <height>51</height>
      </rect>
     </property>
     <property name="text">
      <string>Presión:</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_5">
     <property name="geometry">
      <rect>
       <x>680</x>
       <y>450</y>
       <width>221</width>
       <height>51</height>
      </rect>
     </property>
     <property name="text">
      <string>SpO2:</string>
     </property>
    </widget>
    <widget class="QPlainTextEdit" name="EntradaTemperatura">
     <property name="geometry">
      <rect>
       <x>680</x>
       <y>160</y>
       <width>381</width>
       <height>61</height>
      </rect>
     </property>
    </widget>
    <widget class="QPlainTextEdit" name="PresionEntrada">
     <property name="geometry">
      <rect>
       <x>680</x>
       <y>320</y>
       <width>381</width>
       <height>61</height>
      </rect>
     </property>
    </widget>
    <widget class="QPlainTextEdit" name="Oxigenacion">
     <property name="geometry">
      <rect>
       <x>680</x>
       <y>500</y>
       <width>381</width>
       <height>61</height>
      </rect>
     </property>
    </widget>
    <widget class="QPushButton" name="GuardarSignosVitales">
     <property name="geometry">
      <rect>
       <x>750</x>
       <y>590</y>
       <width>251</width>
       <height>81</height>
      </rect>
     </property>
     <property name="text">
      <string>GUARDAR</string>
     </property>
    </widget>
    <widget class="QComboBox" name="NombresPacientes_2">
     <property name="geometry">
      <rect>
       <x>50</x>
       <y>30</y>
       <width>561</width>
       <height>71</height>
      </rect>
     </property>
     <item>
      <property name="text">
       <string>Omar Perez</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Ricardo Flores</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Jacobo Sanchez</string>
      </property>
     </item>
    </widget>
   </widget>
   <widget class="QWidget" name="Resumen">
    <attribute name="title">
     <string>Resumen del día</string>
    </attribute>
    <widget class="QTableView" name="TablaResumen">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>20</y>
       <width>1041</width>
       <height>761</height>
      </rect>
     </property>
    </widget>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>


