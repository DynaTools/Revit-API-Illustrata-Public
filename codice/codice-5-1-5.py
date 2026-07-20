# -*- coding: utf-8 -*-
__title__ = "Cancella\nModelli di Vista"
__doc__ = "Cancella i modelli di vista del progetto, scelti da una lista."
__author__ = "Ariatta"

import clr
clr.AddReference("RevitAPI")
clr.AddReference("PresentationFramework")
clr.AddReference("PresentationCore")
clr.AddReference("WindowsBase")

from Autodesk.Revit.DB import FilteredElementCollector, View
from pyrevit import revit, forms, script

from System.IO import MemoryStream
from System.Text import Encoding
from System.Windows.Markup import XamlReader

doc = revit.doc

# ---------- Raccogli i modelli di vista ----------
templates = [
    v for v in FilteredElementCollector(doc).OfClass(View)
    if v.IsTemplate
]

if not templates:
    forms.alert("Nessun modello di vista nel progetto.",
                exitscript=True)

template_dict = {t.Name: t for t in templates}

# ---------- Interfaccia (XAML scritto qui, non in un file) ----------
xaml_str = """
<Window xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Cancella modelli di vista"
        Width="420" Height="520"
        WindowStartupLocation="CenterScreen"
        ResizeMode="NoResize">
    <Border Padding="16">
        <Grid>
            <Grid.RowDefinitions>
                <RowDefinition Height="Auto"/>
                <RowDefinition Height="Auto"/>
                <RowDefinition Height="Auto"/>
                <RowDefinition Height="*"/>
                <RowDefinition Height="Auto"/>
                <RowDefinition Height="Auto"/>
            </Grid.RowDefinitions>

            <TextBlock Grid.Row="0" Text="CANCELLA MODELLI DI VISTA" FontSize="15"
                       FontWeight="Bold" Foreground="#2C3E50" Margin="0,0,0,8"/>

            <TextBlock Grid.Row="1" Text="Scegli i modelli da cancellare:"
                       FontSize="12" Foreground="#555" Margin="0,0,0,6"/>

            <StackPanel Grid.Row="2" Orientation="Horizontal" Margin="0,0,0,6">
                <Button x:Name="btn_all" Content="Seleziona tutti"
                        Width="110" Height="24" FontSize="11" Margin="0,0,6,0"/>
                <Button x:Name="btn_none" Content="Deseleziona"
                        Width="110" Height="24" FontSize="11" Margin="0,0,6,0"/>
                <TextBox x:Name="tb_search" Width="150" Height="24"
                         VerticalContentAlignment="Center" FontSize="11"/>
            </StackPanel>

            <ListBox Grid.Row="3" x:Name="lb_templates" Margin="0,0,0,8"
                     SelectionMode="Extended"/>

            <TextBlock Grid.Row="4" x:Name="tb_count"
                       Foreground="#C0392B" FontSize="12" FontWeight="SemiBold"
                       Margin="0,0,0,10"/>

            <StackPanel Grid.Row="5" Orientation="Horizontal"
                        HorizontalAlignment="Right">
                <Button x:Name="btn_delete" Content="Cancella" Width="100" Height="30"
                        IsEnabled="False" Margin="0,0,8,0"
                        Background="#C0392B" Foreground="White" FontWeight="SemiBold"/>
                <Button x:Name="btn_cancel" Content="Annulla" Width="100" Height="30"/>
            </StackPanel>
        </Grid>
    </Border>
</Window>
"""


class DeleteTemplatesUI(object):
    def __init__(self):
        xaml_bytes = Encoding.UTF8.GetBytes(xaml_str)
        stream = MemoryStream(xaml_bytes)
        self.window = XamlReader.Load(stream)

        self.lb_templates = self.window.FindName("lb_templates")
        self.tb_count = self.window.FindName("tb_count")
        self.tb_search = self.window.FindName("tb_search")
        self.btn_all = self.window.FindName("btn_all")
        self.btn_none = self.window.FindName("btn_none")
        self.btn_delete = self.window.FindName("btn_delete")
        self.btn_cancel = self.window.FindName("btn_cancel")

        self.all_names = sorted(template_dict.keys())
        self.selected = []

        for name in self.all_names:
            self.lb_templates.Items.Add(name)

        self.tb_count.Text = "0 di {} selezionati".format(len(self.all_names))

        self.lb_templates.SelectionChanged += self.on_selection
        self.btn_all.Click += self.on_select_all
        self.btn_none.Click += self.on_select_none
        self.btn_delete.Click += self.on_delete
        self.btn_cancel.Click += self.on_cancel
        self.tb_search.TextChanged += self.on_search

    def on_search(self, sender, args):
        query = self.tb_search.Text.lower()
        self.lb_templates.Items.Clear()
        for name in self.all_names:
            if query in name.lower():
                self.lb_templates.Items.Add(name)

    def on_selection(self, sender, args):
        count = self.lb_templates.SelectedItems.Count
        self.tb_count.Text = "{} di {} selezionati".format(
            count, self.lb_templates.Items.Count
        )
        self.btn_delete.IsEnabled = count > 0

    def on_select_all(self, sender, args):
        self.lb_templates.SelectAll()

    def on_select_none(self, sender, args):
        self.lb_templates.UnselectAll()

    def on_delete(self, sender, args):
        self.selected = [
            item for item in self.lb_templates.SelectedItems
        ]
        self.window.DialogResult = True
        self.window.Close()

    def on_cancel(self, sender, args):
        self.window.DialogResult = False
        self.window.Close()

    def show(self):
        return self.window.ShowDialog()


ui = DeleteTemplatesUI()
if not ui.show():
    script.exit()

if not ui.selected:
    script.exit()

# ---------- Conferma ----------
n = len(ui.selected)
msg = "Cancellare {} modelli di vista?".format(n)
if not forms.alert(msg, yes=True, no=True):
    script.exit()

# ---------- Cancella, dentro una Transaction ----------
deleted = 0
with revit.Transaction("Cancella modelli di vista"):
    for name in ui.selected:
        t = template_dict.get(name)
        if t:
            try:
                doc.Delete(t.Id)
                deleted += 1
            except Exception:
                pass

forms.alert("{} modelli cancellati.".format(deleted))
