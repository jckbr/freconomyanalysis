import pandas, bokeh
from bokeh import plotting as bok

pandas.set_option('display.max.colwidth', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
pandas.set_option('display.float_format', '{:.3f}'.format)

dataList = ['API_NY.GDP.MKTP.CD_DS2_en_csv_v2_3731268', 'API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_3628907', 'API_NY.GDP.MKTP.CN_DS2_en_csv_v2_3628879', 'API_NY.GDP.PCAP.CN_DS2_en_csv_v2_3629834', 'API_NY.GDP.PCAP.PP.CD_DS2_en_csv_v2_3630749', 'API_SP.POP.TOTL_DS2_en_csv_v2_3628828', 'API_EN.POP.DNST_DS2_en_csv_v2_3656903', 'API_SE.PRM.NENR_DS2_en_csv_v2_3684068', 'API_SE.SEC.NENR_DS2_en_csv_v2_3662727', 'API_PX.REX.REER_DS2_en_csv_v2_3731960']
rawData = []
figs = []

for file in dataList:
    dataRaw = pandas.read_csv('Data/' + file + '/' + file + '.csv', skiprows=4)
    data = dataRaw[dataRaw['Country Name'] == 'France']
    dataDesc = data['Indicator Name']
    dataTrim = data.iloc[:, 4:].T
    dataTrim.rename(columns={77: 'France'}, inplace=True)
    dataTrim.reset_index(inplace=True)
    dataTrim = dataTrim.iloc[-12:, :]
    dataTrimSrc = bok.ColumnDataSource(dataTrim)
    rawData.append(dataTrim)
    fig = bok.figure(title=dataDesc.item())
    fig.line(x='index', y='France', source=dataTrimSrc)
    fig.left[0].formatter.use_scientific = False
    figs.append(fig)

bok.show(bokeh.layouts.column(figs))

data2010 = pandas.read_csv('Data/FranceImportExportData2010.csv')
data2019 = pandas.read_csv('Data/FranceImportExportData2019.csv')
data2010 = data2010.iloc[:, [1,2,16,18,22]]
data2019 = data2019.iloc[:, [1,2,16,18,22]]
data2010['Export Trade Value (US$ Thousand)'] = data2010['Export Trade Value (US$ Thousand)'].replace('[\$,]','',regex=True).astype(float)
data2010['Import Trade Value (US$ Thousand)'] = data2010['Import Trade Value (US$ Thousand)'].replace('[\$,]','',regex=True).astype(float)
data2019['Export Trade Value (US$ Thousand)'] = data2019['Export Trade Value (US$ Thousand)'].replace('[\$,]','',regex=True).astype(float)
data2019['Import Trade Value (US$ Thousand)'] = data2019['Import Trade Value (US$ Thousand)'].replace('[\$,]','',regex=True).astype(float)

data2010Export = data2010.groupby(['ProductGroupDescription']).sum().sort_values(['Export Trade Value (US$ Thousand)'], ascending=False)
data2010Export['Export %'] = 100 * (data2010Export['Export Trade Value (US$ Thousand)'] / data2010Export['Export Trade Value (US$ Thousand)'].sum())
data2010ExportMarket = data2010.groupby(['Partner Product Break down']).sum().sort_values(['Export Trade Value (US$ Thousand)'], ascending=False)
data2010ExportMarket['Export %'] = 100 * (data2010ExportMarket['Export Trade Value (US$ Thousand)'] / data2010ExportMarket['Export Trade Value (US$ Thousand)'].sum())
data2010Import = data2010.groupby(['ProductGroupDescription']).sum().sort_values(['Import Trade Value (US$ Thousand)'], ascending=False)
data2010Import['Import %'] = 100 * (data2010Import['Import Trade Value (US$ Thousand)'] / data2010Import['Import Trade Value (US$ Thousand)'].sum())
data2010ImportMarket = data2010.groupby(['Partner Product Break down']).sum().sort_values(['Import Trade Value (US$ Thousand)'], ascending=False)
data2010ImportMarket['Import %'] = 100 * (data2010ImportMarket['Import Trade Value (US$ Thousand)'] / data2010ImportMarket['Import Trade Value (US$ Thousand)'].sum())
data2019Export = data2019.groupby(['ProductGroupDescription']).sum().sort_values(['Export Trade Value (US$ Thousand)'], ascending=False)
data2019Export['Export %'] = 100 * (data2019Export['Export Trade Value (US$ Thousand)'] / data2019Export['Export Trade Value (US$ Thousand)'].sum())
data2019ExportMarket = data2019.groupby(['Partner Product Break down']).sum().sort_values(['Export Trade Value (US$ Thousand)'], ascending=False)
data2019ExportMarket['Export %'] = 100 * (data2019ExportMarket['Export Trade Value (US$ Thousand)'] / data2019ExportMarket['Export Trade Value (US$ Thousand)'].sum())
data2019Import = data2019.groupby(['ProductGroupDescription']).sum().sort_values(['Import Trade Value (US$ Thousand)'], ascending=False)
data2019Import['Import %'] = 100 * (data2019Import['Import Trade Value (US$ Thousand)'] / data2019Import['Import Trade Value (US$ Thousand)'].sum())
data2019ImportMarket = data2019.groupby(['Partner Product Break down']).sum().sort_values(['Import Trade Value (US$ Thousand)'], ascending=False)
data2019ImportMarket['Import %'] = 100 * (data2019ImportMarket['Import Trade Value (US$ Thousand)'] / data2019ImportMarket['Import Trade Value (US$ Thousand)'].sum())

print('2010 Exports', data2010Export.sort_values(by='Export Trade Value (US$ Thousand)', ascending=False)[['Export Trade Value (US$ Thousand)', 'Export %']].iloc[:10, :])
print('\n2010 Export Markets', data2010ExportMarket.sort_values(by='Export Trade Value (US$ Thousand)', ascending=False)[['Export Trade Value (US$ Thousand)', 'Export %']].iloc[:10, :])
print('\n2010 Imports', data2010Import.sort_values(by='Import Trade Value (US$ Thousand)', ascending=False)[['Import Trade Value (US$ Thousand)', 'Import %']].iloc[:10, :])
print('\n2010 Import Markets', data2010ImportMarket.sort_values(by='Import Trade Value (US$ Thousand)', ascending=False)[['Import Trade Value (US$ Thousand)', 'Import %']].iloc[:10, :])
print('\n2019 Exports', data2019Export.sort_values(by='Export Trade Value (US$ Thousand)', ascending=False)[['Export Trade Value (US$ Thousand)', 'Export %']].iloc[:10, :])
print('\n2019 Export Markets', data2019ExportMarket.sort_values(by='Export Trade Value (US$ Thousand)', ascending=False)[['Export Trade Value (US$ Thousand)', 'Export %']].iloc[:10, :])
print('\n2019 Imports', data2019Import.sort_values(by='Import Trade Value (US$ Thousand)', ascending=False)[['Import Trade Value (US$ Thousand)', 'Import %']].iloc[:10, :])
print('\n2019 Import Markets', data2019ImportMarket.sort_values(by='Import Trade Value (US$ Thousand)', ascending=False)[['Import Trade Value (US$ Thousand)', 'Import %']].iloc[:10, :])

print('\n2010 Export count:', data2010Export.shape[0])
print('2010 Export market count:', data2010ExportMarket.shape[0])
print('2010 Import count:', data2010Import.shape[0])
print('2010 Import market count:', data2010ImportMarket.shape[0])
print('2019 Export count:', data2019Export.shape[0])
print('2019 Export market count:', data2019ExportMarket.shape[0])
print('2019 Import count:', data2019Import.shape[0])
print('2019 Import market count:', data2019ImportMarket.shape[0])

print('\n2010 Total Exports:', data2010Export['Export Trade Value (US$ Thousand)'].sum() * 1000)
print('2010 Total Imporst:', data2010Import['Import Trade Value (US$ Thousand)'].sum() * 1000)
print('2010 GDP (current US$):', rawData[0].iloc[0, 1])
print('2010 Total Exports:', data2019Export['Export Trade Value (US$ Thousand)'].sum() * 1000)
print('2010 Total Imporst:', data2019Import['Import Trade Value (US$ Thousand)'].sum() * 1000)
print('2010 GDP (current US$):', rawData[0].iloc[-3, 1])

print('\n2010 Openness:', ((data2010Export['Export Trade Value (US$ Thousand)'].sum() * 1000) + (data2010Import['Import Trade Value (US$ Thousand)'].sum() * 1000)) / rawData[0].iloc[0, 1])
print('2019 Openness:', ((data2019Export['Export Trade Value (US$ Thousand)'].sum() * 1000) + (data2019Import['Import Trade Value (US$ Thousand)'].sum() * 1000)) / rawData[0].iloc[-3, 1])

print('\n2010 Balance of trade:', (data2010Export['Export Trade Value (US$ Thousand)'].sum() * 1000) - (data2010Import['Import Trade Value (US$ Thousand)'].sum() * 1000))
print('2019 Balance of trade:', (data2019Export['Export Trade Value (US$ Thousand)'].sum() * 1000) - (data2019Import['Import Trade Value (US$ Thousand)'].sum() * 1000))

print('\n2010 Export List:', data2010Export['Export %'])
print('2019 Export List:', data2019Export['Export %'])

print('\n2010 Export Market List:', data2010ExportMarket['Export %'])
print('2019 Export Market List:', data2019ExportMarket['Export %'])