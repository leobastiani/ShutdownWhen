object MainForm: TMainForm
  Left = 0
  Top = 0
  BorderIcons = [biSystemMenu, biMinimize]
  BorderStyle = bsSingle
  Caption = 'shutdownWss'
  ClientHeight = 241
  ClientWidth = 729
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  OnClose = FormClose
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object novaFotoBtn: TButton
    Left = 8
    Top = 8
    Width = 121
    Height = 37
    Caption = 'Nova Foto'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -16
    Font.Name = 'Tahoma'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 0
    OnClick = novaFotoBtnClick
  end
  object compararBtn: TButton
    Left = 144
    Top = 8
    Width = 121
    Height = 37
    Caption = 'Comparar'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -16
    Font.Name = 'Tahoma'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 1
    OnClick = compararBtnClick
  end
  object cortarBtn: TButton
    Left = 280
    Top = 8
    Width = 121
    Height = 37
    Caption = 'Cortar'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -16
    Font.Name = 'Tahoma'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 2
    OnClick = cortarBtnClick
  end
  object grupoImagemOriginal: TGroupBox
    Left = 8
    Top = 51
    Width = 209
    Height = 154
    Caption = 'Imagem Original'
    TabOrder = 3
    object Imagem: TImage
      Left = 16
      Top = 24
      Width = 0
      Height = 0
      Margins.Left = 0
      Margins.Top = 0
      Margins.Right = 0
      Margins.Bottom = 0
      ParentShowHint = False
      ShowHint = False
      OnMouseDown = ImagemMouseDown
      OnMouseMove = ImagemMouseMove
      OnMouseUp = ImagemMouseUp
    end
    object Shape: TShape
      Left = 141
      Top = 33
      Width = 65
      Height = 65
      Brush.Style = bsClear
      Pen.Color = clGreen
      Pen.Width = 3
    end
  end
  object cursorBtn: TButton
    Left = 8
    Top = 211
    Width = 75
    Height = 26
    Caption = 'Cursor'
    TabOrder = 4
    OnClick = cursorBtnClick
  end
  object recortarBtn: TButton
    Left = 89
    Top = 211
    Width = 75
    Height = 26
    Caption = 'Recortar'
    TabOrder = 5
    OnClick = recortarBtnClick
  end
  object Comando: TLabeledEdit
    Left = 407
    Top = 24
    Width = 257
    Height = 21
    EditLabel.Width = 49
    EditLabel.Height = 13
    EditLabel.Caption = 'Comando:'
    Font.Charset = ANSI_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Lucida Console'
    Font.Style = []
    ParentFont = False
    TabOrder = 6
    Text = 'shutdown -s -t 60 -hybrid'
  end
  object Console: TMemo
    Left = 406
    Top = 51
    Width = 314
    Height = 186
    Font.Charset = ANSI_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Lucida Console'
    Font.Style = []
    ParentFont = False
    ReadOnly = True
    ScrollBars = ssBoth
    TabOrder = 7
  end
  object execBtn: TButton
    Left = 670
    Top = 20
    Width = 51
    Height = 25
    Caption = 'Executar'
    TabOrder = 8
    OnClick = execBtnClick
  end
  object cancelarBtn: TButton
    Left = 326
    Top = 211
    Width = 75
    Height = 26
    Caption = 'Cancelar'
    Enabled = False
    TabOrder = 9
    OnClick = cancelarBtnClick
  end
  object settingsGroup: TGroupBox
    Left = 231
    Top = 51
    Width = 170
    Height = 154
    Caption = 'Configura'#231#245'es'
    TabOrder = 10
    object lentoBtn: TButton
      Left = 15
      Top = 24
      Width = 50
      Height = 25
      Caption = 'Lento'
      TabOrder = 0
      OnClick = lentoBtnClick
    end
    object rapidoBtn: TButton
      Left = 71
      Top = 24
      Width = 49
      Height = 25
      Caption = 'R'#225'pido'
      TabOrder = 1
      OnClick = rapidoBtnClick
    end
    object secIntervalEdt: TLabeledEdit
      Left = 15
      Top = 69
      Width = 50
      Height = 21
      EditLabel.Width = 109
      EditLabel.Height = 13
      EditLabel.Caption = 'Intervalo de Teste (s):'
      TabOrder = 2
      Text = '60'
      OnExit = NovosValores
    end
    object countdownEdt: TLabeledEdit
      Left = 15
      Top = 115
      Width = 50
      Height = 21
      EditLabel.Width = 147
      EditLabel.Height = 13
      EditLabel.Caption = 'Tempo m'#225'ximo de espersa (s):'
      TabOrder = 3
      Text = '180'
      OnChange = NovosValores
      OnExit = NovosValores
    end
  end
  object autoComparar: TTimer
    Enabled = False
    OnTimer = autoCompararTimer
    Left = 32
    Top = 104
  end
end
