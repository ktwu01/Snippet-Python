# MATLAB Head Function

## Licences

licstatus

  

wukoutian@casper20:~> licstatus

  

                                       Me | Used | Total

---------------------------------------------------------

   |-- MATLAB_Distrib_Comp_Engine:      0 |    0 |   400

  

 MATLAB:                                0 |   12 |    50

   |-- Neural_Network_Toolbox:          0 |    0 |     1

   |-- Image_Toolbox:                   0 |    0 |     5

   |-- MATLAB_Builder_for_Java:         0 |    0 |     1

   |-- Compiler:                        0 |    0 |     1

   |-- MAP_Toolbox:                     0 |    1 |     5

   |-- Optimization_Toolbox:            0 |    1 |     2

   |-- Distrib_Computing_Toolbox:       0 |    1 |    10

   |-- Signal_Toolbox:                  0 |    1 |     6

   |-- Statistics_Toolbox:              0 |    5 |    25

   |-- Identification_Toolbox:          0 |    1 |     2

  

 PGI:                                   0 |    0 |     0

  
  

## Set all Fontsize in one figure: FastX fs = 30; Win fs = 12-14

set(findall(gcf,'-property','FontSize'),'FontSize', fs);

  

fs = 30; % fontsize

  
  

## Functions bkup in Google drive

1. Change the code name
    
2. D:\0lrn\0Res\Data\
    
3. For analysis data: save 2023
    
4. Change the date and year
    

years = 2014: 2023;

DAY_PER = datenum(years (end),12,31)- datenum(years (1),1,1)+1

2014--> years (1)

2022--> years (end)

2023--> years (end)

3287 change to àDAY_PER

3288 change to àDAY_PER+1

Change the name of the variables: 9yrs

5.   
    
6. Save: daily or ave.
    
7. disp('All Data Saved! Please Check!')
    

  

## try-catch

try

    % Your code that might cause an error goes here

    % e.g. a fitting function

catch ME

    % This block will execute if there's an error in the try block

    disp('An error occurred:');

    disp(ME.message);

    % You can add additional code here to handle the error or just skip it

end

  

# NAMING rules

% % % % % % parameters: start from startyear-01-01, end in endyear-12-31

% naming format of files: Site/Equipments_parameter1_parameter2_parameter3_startyear_endyear.mat

% no need for index

% do not use construct

% for different Site/Equipments, use different prefix

  
  

# Indexing

selected_day = datenum(2022,10,02);

inds = find(mcest>24*(selected_day- datenum(2014,01,01)) & mcest<24*(selected_day+1- datenum(2014,01,01)));

  

# Head Config

## Read fileInfo

  

% fileInfo = whos('-file', loadfilename); data = load(loadfilename, fileInfo.name); bjmet = data.(fileInfo.name);

  

## %% Update meteor parameters

directoryPath = 'D:\0lrn\0Res\Data\';

baseFilename = 'A0_Stations_Para_';

WKT_runLatestVersion(directoryPath, baseFilename);

load('D:\0lrn\0Res\Data\MR_Stations_Para.mat');

  

## %% Know station name, find station id

% site: station name, ST_id: station id in D:\0lrn\0Res\Data\MR_Stations_Para.mat

ST_id = WKT_findStringMatch(site, STs, sites)

  
  

## Read2

%% !!! Please check whether to change the savename first!!!

%% !!! Please check whether to change the savename first!!!

clear all; clc; close all; time_sys1=clock;

addpath 'D:\0lrn\0Res\Functions'

%% config

site = 'Mh'

years = 2011:2021

  

% site = 'Bj'

% years = 2011:2023

% site = 'Mc'

% years = 2014:2023

% site = 'Wh'

% years = 2010:2023

  

% site = 'Km'

% years = 2011:2014

  

Target_Year = years(end-1)

deltaT = 8

  

% site = 'Dv'

%

% years = 2005:2005

% Target_Year = years(1)

% deltaT = 5+20/60

loadfilename = sprintf('D:\\0lrn\\0Res\\Data\\%sMRdata_%d_%d.mat', site, years(1), years(end))

loadfilename1 = sprintf('D:\\0lrn\\0Res\\Data\\%s_ids_%d.mat', site, Target_Year)

load(loadfilename, 'azimuth','mcrd','localtime','speed');

load(loadfilename1);

  

% Construct the filename using savefilename1

savefilename1 = ...

sprintf('D:\\0lrn\\0Res\\Data\\%s_sp_dis_daily_%d_%d.mat', site, years(1), years(end))

% Construct the filename using savefilename2

savefilename2 = ...

sprintf('D:\\0lrn\\0Res\\Data\\%s_sp_dis_ave_%d_%d.mat', site, years(1), years(end))

  

% load('D:\0lrn\0Res\Data\BjMRdata_2011_2023.mat')

  
  

% % % % % % parameters: start from startyear-01-01, end in endyear-12-31

% naming format of files: Site/Equipments_parameter1_parameter2_parameter3_startyear_endyear.mat

% no need for index

% do not use construct

% for different Site/Equipments, use different prefix

  

# Load

load('../../Data/Mc_sp_dis_ave_2014_2023.mat');

addpath '../../Functions'

  

D:\0lrn\0Res\ = ..\..\

  

load(loadfilename, ...

'mcest','mch','mczenith', ...

'azimuth','speed','number','localtime','doy');

load('D:\0lrn\0Res\Data\OptionalMMRdata2014_2022.mat', ...

'azimuth','doy','localtime','mcest','speed');

load(['D:\0lrn\0Res\Data\ids2014_2022.mat']);

load('D:\0lrn\0Res\ITDP\Data\whh_num_pk&wid_2010_2023.mat');

load('D:\0lrn\0Res\ITDP\Data\whh_num_pk&wid_2010_2023.mat', ...

'whnum','whhpeak','whhwidth');

load('D:\0lrn\0Res\ITDP\Data\OptionalMMRdata2014_2022.mat', ...

'mch','mcest','localtime','mcrd','azimuth');

  
  

# Color

## Dark Color series (distinct)

ST_clos = {'r', 'g', 'b', 'c', 'm', [0.8500 0.3250 0.0980], 'k', [0.5, 0.2, 0.8], [0.1, 0.9, 0.2]};

  

## Color series (gradually 渐变)

% specify the target observation stations

TarSTs = {'SCOMR', 'ALOMR', 'LCOMR', 'DVMR', 'MCMR', 'WHMR', 'BJMR', 'MHMR', 'ALTMR'};

% Define the orientation

ORIENT = {'E', 'E', 'E', 'W', 'W', 'W', 'W', 'W', 'W' };

  

% % Define colors for each station, these can be RGB triples or color names

% ST_clos = {'r', 'g', 'b', 'c', 'm', [0.8500 0.3250 0.0980], 'k', [0.5, 0.2, 0.8], [0.1, 0.9, 0.2]};

  

ST_clos = num2cell(cmap(1:7:1-7+7*numel(TarSTs), :), 2);

  
  

## Colormap

  

clen=30; % the bigger clen is, the more smmoth

saturation=1.0 % the bigger saturation is, the more saturate

cmap = nph_saturate(cbrew('nph_RdYlBu',clen),saturation);

hold on; colormap(gca,cmap); colorbar;

testnum=rand(21,13);testnum=log(testnum/max(max(testnum)));

conlevel = 60; contourf(0:2:24,0:4:80,testnum,conlevel,'Linestyle','none');

%%%% COLORBAR

cbar = nph_colorbar;

cbar.Label.String = ['log_{10}(N/N_{max})'];

% cbar.Ticks = [-7 -5 -3 -1 0];

cbar.Ticks = -8:2:0;

cbar.TickDirection = 'out';

cbar.Position = cbar.Position .* [1 1 0.8 1];

cbar.Position = cbar.Position + [-0.5*cbar.Position(3) 0 0 0];

% cbar.Label.String = ['\bf{' clabs{ax} '}'];

cbar.Label.Rotation = 90;

  
  

% nph_Spectral

% nph_modspectral

% nph_RdBuPastel

% nph_Rainbow

% nph_RainbowWhite

% nph_BlueOrange

% nph_BuOrRd

% nph_RdYlBuGrey

% nph_OSDiv1

% nph_OSDiv2

  

   cmap = nph_saturate(cbrew('nph_RdYlBuGrey',Con_lev),1.0);

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeK6FextLwM_03Uo8O5Jn7MD_3jj6_SM3CtiR6-2D2Sc0dZbJUWgdwBgXXaAPSLEQOSI2t46-t2MaNpJsz_hc5v8I7ckcGhfw6Zd6uMglIstEsA0RafeRK7Ms5luOd1B2X4sH8PO4O_BjfdfCEfOmuU4bhq?key=ZvK41nUrbPTqk1kEvSmcbg)

  

## barcolor bar color

% Example: barcolor = '#0065a1';

barcolor = '#009BCA';

dashcolor= '#dfdfdf';

sphistcolor1 = '#4B6099';

sphistcolor2 = '#5E71A9';

sphistcolor3 = '#8086BA';

sphistcolor4 = '#9692C5';

sphistcolor5 = '#B6A7D2';

sphistcolor6 = '#C7B3CC';

sphistcolor7 = '#D6B7C7';

sphistcolor8 = '#E4BEBB';

sphistcolor9 = '#F1C5A8';

sphistcolor10 = '#FAC897';

sphistcolor11 = '#EFB285';

sphistcolor12 = '#A8736B';

  
  

# Date <–> string

  

title(datestr((datenum(2022,10,02)),'mmm dd, yyyy'));

  

selected_day = datenum(2022,10,02);

title(datestr((selected_day),'mmm dd, yyyy'));

  

st_n = datenum(2022,2,1); %% Start date

en_n = datenum(2022,2,7); %% End date

for dn = st_n:en_n

day = datestr(dn,30); %% YYYYMMDD

end

  
  

# Years label

years = {};

years = 2010:2023;

xtickYrs(gca, years, dashcolor);

xtickYrslabel(gca, years,fs);

  
  

function xtickYrs(gca, years, dashcolor)

xlim([0 datenum((max(years)+1),01,01)-datenum(min(years),01,01)]);

hold on;grid on; axx=gca;

  

% Just show the Januarys as major ticks

axx.XTick = datenum(min(years):(max(years)+1),01,01)-datenum(min(years),01,01);

axx.XMinorTick = 'on';

axx.XAxis.MinorTickValues = datenum(min(years),1:((length(years)+1)*12),01)-datenum(min(years),01,01);

datetick('x','m','keepticks','keeplimits');

axx.XTickLabel = {};

  

% add dashed lines to the Januarys except the first Jan

dashday = datenum((min(years)):(max(years)+1),01,01)-datenum(min(years),01,01);

for xt = dashday

if inrange(xt,xlim)% && ~any(xt == axx.XTick)

hold on; plot([xt xt],axx.YLim,'linest','--','color',dashcolor,'linewi',axx.LineWidth);

% text(xt,-500./1000,mn(1),'fontsize',0.9*fs,'horizontalalignment','center','VerticalAlignment','top');

end

end

  

end

  
  
  
  

function xtickYrslabel(gca, years, fs)

xlim([0 datenum((max(years)+1),01,01)-datenum(min(years),01,01)]);

  

hold on;grid on; axx=gca;

  

% Januarys and Junes as labels using text:

ytix1 = min(gca().YLim)-(max(gca().YLim)-min(gca().YLim))*0.05;

xtixJan = datenum(years(1),1:12:(length(years)*12+1),2)-datenum(min(years)-1,12,31);

for xt = xtixJan

% if inrange(xt,xlim) % && ~any(xt == axx.XTick)

mn = monthname(month(xt),'mmm');

text(xt,ytix1,mn,'fontsize',fs,'horizontalalignment','center','VerticalAlignment','top');

% end

end

  

xtixJul = datenum(years(1),7:12:(length(years)*12+7),2)-datenum(min(years)-1,12,31);

for xt = xtixJul

if inrange(xt,xlim) % && ~any(xt == axx.XTick)

mn = monthname(month(xt),'mmm');

text(xt,ytix1,mn,'fontsize',fs,'horizontalalignment','center','VerticalAlignment','top');

end

end

  

% % other months as labels using text:

% xtix = datenum(years(1),1:(length(years)*12),15)-datenum(min(years)-1,01,01);

% for xt = xtix

% if inrange(xt,xlim) && ~any(xt == axx.XTick)

% mn = monthname(month(xt));

% text(xt,-500./1000,mn(1),'fontsize',fs,'horizontalalignment','center','VerticalAlignment','top');

% end

% end

  

% Years as lower numbers:

ytix2 = min(gca().YLim)-(max(gca().YLim)-min(gca().YLim))*0.17;

xtix2 = datenum(years,07,01)-datenum(min(years),01,01);

for xt = xtix2

if inrange(xt,xlim) && ~any(xt == axx.XTick)

yrstr = datestr(xt,'yyyy');

yrstr = num2str(str2double(yrstr) + min(years));

% bold number

% text(xt,ytix2,yrstr,'fontsize',1*fs,'fontweight','bold','horizontalalignment','center','VerticalAlignment','top');

text(xt,ytix2,yrstr,'fontsize',1*fs,'horizontalalignment','center','VerticalAlignment','top');

end

end

  

end

  
  

function xticknyrs(gca, years, dashcolor)

daysn = datenum(years(end),12,31)-datenum(years(1),01,01)+1;

xlim([0 daysn]);

hold on;grid on; axx=gca;

figure;

whitefig;figpos([0.5 0.5])

subplot(2,1,1)

  

%-------------------------------------------------------

vert_gap = 0.1; horz_gap = 0.0;

lower_marg = 0.05; upper_marg = 0.03;

left_marg = 0.06; right_marg = 0.11;

rows = 2; cols = 1;

subplot = @(rows,cols,p) subtightplot (rows,cols,p,[vert_gap horz_gap],[lower_marg upper_marg],[left_marg right_marg]);

%--------------------------------------------------------

fs = 12; % fontsize

  
  

%%

for ax = 1:6

subplot(rows,cols,ax);

axx = gca;

setfont(fs);

set(gca,'linewi',1,'tickdir','out');

hold on; nph_text([0.0 0.875],['(' alphabet(ax) ')'],'fontsize',1.75*fs);

% hold on; nph_text([0.025 0.865],['(' alphabet(ax) ')'],'fontsize',1.75*fs,'textborder','w');

end

% Just show the Januarys as major ticks

axx.XTick = datenum(years,01,01)-datenum(years(1),01,01);

axx.XMinorTick = 'on';

axx.XAxis.MinorTickValues = datenum(min(years),1:((length(years)+1)*12),01)-datenum(years(1),01,01);

datetick('x','m','keepticks','keeplimits');

axx.XTickLabel = {};

  

% add dashed lines to the Januarys except the first Jan

dashday = datenum(years(2):years(end),01,01)-datenum(years(1),01,01);

for xt = dashday

if inrange(xt,xlim)% && ~any(xt == axx.XTick)

hold on; plot([xt xt],axx.YLim,'linest','--','color',dashcolor,'linewi',axx.LineWidth);

% text(xt,-500./1000,mn(1),'fontsize',0.9*fs,'horizontalalignment','center','VerticalAlignment','top');

end

end

end

function xticknyrslabel(gca, years, fs)

daysn = datenum(years(end),12,31)-datenum(years(1),01,01)+1;

xlim([0 daysn]);

hold on;grid on; axx=gca;

% Januarys and Junes as labels using text:

ytix1 = min(gca().YLim)-(max(gca().YLim)-min(gca().YLim))*0.05;

xtixJan = datenum(years(1),1:12:(length(years)*12+1),2)-datenum(years(1)-1,12,31);

for xt = xtixJan

% if inrange(xt,xlim) % && ~any(xt == axx.XTick)

mn = monthname(month(xt),'mmm');

text(xt,ytix1,mn,'fontsize',fs,'horizontalalignment','center','VerticalAlignment','top');

% end

end

xtixJul = datenum(years(1),7:12:(length(years)*12+7),2)-datenum(years(1)-1,12,31);

for xt = xtixJul

if inrange(xt,xlim) % && ~any(xt == axx.XTick)

mn = monthname(month(xt),'mmm');

text(xt,ytix1,mn,'fontsize',fs,'horizontalalignment','center','VerticalAlignment','top');

end

end

% % other months as labels using text:

% xtix = datenum(years(1),1:(length(years)*12),15)-datenum(2014,01,01);

% for xt = xtix

% if inrange(xt,xlim) && ~any(xt == axx.XTick)

% mn = monthname(month(xt));

% text(xt,-500./1000,mn(1),'fontsize',fs,'horizontalalignment','center','VerticalAlignment','top');

% end

% end

% Years as lower numbers:

ytix2 = min(gca().YLim)-(max(gca().YLim)-min(gca().YLim))*0.17;

xtix2 = datenum(years,07,01)-datenum(years(1),01,01);

for xt = xtix2

if inrange(xt,xlim) && ~any(xt == axx.XTick)

yrstr = datestr(xt,'yyyy');

yrstr = max(double(yrstr))+years(1)-56+8;

yrstr = int2str(yrstr);

% bold number

% text(xt,ytix2,yrstr,'fontsize',1*fs,'fontweight','bold','horizontalalignment','center','VerticalAlignment','top');

text(xt,ytix2,yrstr,'fontsize',1*fs,'horizontalalignment','center','VerticalAlignment','top');

end

end

end

  
  

# One Year label

mttk1yr(gca,fs)

  

function mttk1yr(gca,fs)

xlim([0 365]);

axx=gca;

axx.XTick = datenum(2014,1:12,1)-datenum(2014,01,01);

hold on; datetick('x','m','keepticks','keeplimits')

axx.XTickLabel = {};

  

% % % months as ticks using text at 15th day

% % ytix1 = min(gca().YLim)-(max(gca().YLim)-min(gca().YLim))*0.05;

% % xtixMt = datenum(2014,1:12,15)-datenum(2014,01,01);

% % for xt = xtixMt

% % if inrange(xt,xlim)

% % mn = monthname(month(xt),'mmm');

% % hold on; text(xt,ytix1,mn,'fontsize',fs,'horizontalalignment','center','VerticalAlignment','top');

% % end

% % end

axx.XMinorTick = 'off';

  

xpt(1) = datenum(2014,1,4)-datenum(2014,01,01);

% ypt(1) = 30;

npt{1} = {'Perihelion','Jan 4'};

  

xpt(2) = datenum(2014,4,4)-datenum(2014,01,01);

% ypt(2) = 57;

npt{2} = {'Spring','Apr 4'};

  

xpt(3) = datenum(2014,7,4)-datenum(2014,01,01);

% ypt(3) = 31 ;

npt{3} = {'Aphelion','Jul 4'};

  

xpt(4) = datenum(2014,10,2)-datenum(2014,01,01);

% ypt(4) = 59;

npt{4} = {'Autumn','Oct 2'};

  

%% legend: lines indicate selected 4 points

for xt = xpt

if inrange(xt,xlim)

hold on; plot([xt xt],axx.YLim,'linest','--','color','k','linewi',axx.LineWidth);

end

end

  

% %% legend: text indicate selected 4 points

% hold on; text(xpt,5.5*ones(size(xpt)),npt,'fontsize',0.8*fs,'horizontalalignment','center','VerticalAlignment','top');

  

end

  
  

# Ylabel

ylabel('Height Width (km)');

ylabel('Peak height (km)');

speed 改velocity

  

# Title

## Splitting

title({'Azimuth versus number : Jan 4';''})

;'';'';''})

  

## nph_text textborder

  

'FontSize',fs); % ,'textborder','w');

  

## Characters connect to one line

N = 100; % N greater, the more precise

for k1=1:length(sites)

[dist(k1),~,~] = m_lldist([TGlon lons(k1)], [TGlat lats(k1)],N);

end

  

[string(sites{k1})+' ('+string(STs{k1})+', '+string(round(dist(k1)))+' km, '+num2str(freqs(k1))+' MHz)']

  

sprintf('%s - %d km',cities{k1},round(range))

% sgtitle({['Site @ '+string(upper(site))];' ';' ';' '});

sgtitle(['Site @ ' + string(upper(site)) + newline + newline + newline]);

%% sgtitle

fname_with_space = [string(ST)+ ' Wind 220114 220118'];

title_name = [string(sites{ST_id})+' ['+string(STs{ST_id})+', '+string((lats(ST_id)))+' (E+/W-) '+', '+string((lons(ST_id)))+' (N+/S-) '+', '+string(round(dist(ST_id)))+' km, '+num2str(freqs(ST_id))+' MHz]']

sgtitle(title_name);

% title([num2str(time(k)) ' days since 0001-01-20 04:35:00'])

  

## WKT_setTightMargin(

  

ax = gca;

WKT_setTightMargin(ax, 'TightInset');

% WKT_setTightMargin(ax, 'fixed');

function WKT_setTightMargin(ax, method)

% Function: WKT_setTightMargin

% Description: Sets tight margins for a given axes handle based on the specified method.

% Input: ax - handle to the axes

%        method - a string, either 'TightInset' or 'fixed' to choose the margin setting method

  

    % Validate the input arguments to ensure they are of the correct type

    if nargin < 2

        error('Both axes handle and method are required.');

    end

    if ~ishandle(ax) || ~strcmp(get(ax,'Type'),'axes')

        error('First argument must be a handle to axes.');

    end

    if ~ischar(method) || ~ismember(method, {'TightInset', 'fixed'})

        error('Second argument must be a string either "TightInset" or "fixed".');

    end

  

    % Set margins based on TightInset

    if strcmp(method, 'TightInset')

        % Get the TightInset values from the current axes

        tight_inset = get(ax, 'TightInset');

        % Define additional custom margins [left, bottom, right, top]

        custom_margin = [0.0, 0.055, 0.0, 0.055];

        % Add the custom margins to the TightInset values

        % and set them as the new LooseInset for the axes

        set(ax, 'LooseInset', tight_inset + custom_margin);

    % Set fixed custom margins

    elseif strcmp(method, 'fixed')

        % Define fixed custom margins [left, bottom, right, top]

        fixed_custom_margin = [0.0, 0.055, 0.0, 0.055];

        % Directly set the fixed custom margins as the LooseInset for the axes

        set(ax, 'LooseInset', fixed_custom_margin);

    end

  

end

  
  

# SET SUBPLOT

%%

for ax = 1:2

fs = 12;

subplot(1,2, ax);

axx = gca;

setfont(fs);

set(gca,'linewi',1,'tickdir','out');

hold on; nph_text([-0.1 0.875],['(' alphabet(ax) ')'],'fontsize',1.75*fs);

end

  
  

## Scale bar scalebar

RRtio = 10;

 ax1 = subplot(rows,cols,1);

 % Add the scale bar only to the first subplot

 exScale = 10;

 bar_height = RRtio * exScale;

 x_position = 5.5;

 y_position = 10350;

 WKT_addScaleBar(ax1, x_position, y_position, bar_height, exScale);

hold on

  

function WKT_addScaleBar(ax, x_position, y_position, bar_height, exScale)

global fs

ScaleBarLinWi = 1.5;

axes(ax);

hold on

line([x_position, x_position], [y_position - bar_height/2, y_position + bar_height/2], 'Color', 'k', 'LineWidth', ScaleBarLinWi);

cap_width = 0.5;

line([x_position - cap_width/2, x_position + cap_width/2], [y_position - bar_height/2, y_position - bar_height/2], 'Color', 'k', 'LineWidth', ScaleBarLinWi);

line([x_position - cap_width/2, x_position + cap_width/2], [y_position + bar_height/2, y_position + bar_height/2], 'Color', 'k', 'LineWidth', ScaleBarLinWi);

text(x_position + cap_width, y_position, sprintf('%d m/s', exScale), 'HorizontalAlignment', 'left', 'VerticalAlignment', 'middle', 'FontSize', fs);

end

  
  

# SAVE EXPORT FIG

error;

%% EXPORT FIG =================================

set(gcf, 'Renderer', 'painters');

figure_name = ['Fig10'];

print(gcf,figure_name,'-djpeg','-r600');

% saveas(gcf,figure_name,'svg');

% print(gcf,['Figure7_'+string(site)],'-dpng','-r600');

% saveas(gcf,['Figure9_'+string(site)],'epsc')

disp('Figure Saved.');

% exportgraphics(gcf,'Tonga_Zonal wind_lev1_85-135e_15-50n_ut12-21.gif','Append',true);

  

# Prompts that might not usually be used

  

# Prompt:  using matlab code to read the following TXT data, and get the column 2 and column 3 data as time and Magnetic field.

turn the time "14:39:22.414" to time described using hour, and turn the "40513.1924" to a "double" data.

prompt: connect the following variables and their sub-1 together, seperately, like: mcest=[mcmet, mcmet1]; mch= [mch, mch1],  and give the matlab code. 'Mcest','mch','mczenith','azimuth','speed','mcr','number','mcrd','localtime','doy'

  

# Prompt: 用matlab高斯拟合带有一个peak的分段函数, 并且求出峰值.

第1段函数是 从负无穷到mu的以mu为均值,以sigma1为方差的高斯分布

第2段函数是 从mu到正无穷的以mu为均值,以sigma2为方差的高斯分布

注释使用英文. 尽量使用matlab自带函数, 不要使用"Toolbox."

  

# Prompt:  用matlab谐波拟合带有一个peak的一维分布图, 并且求出峰值. x 函数是均匀的,而y函数不是均匀的. 注释使用英文. 尽量使用matlab自带函数, 不要使用"Statistics and Machine Learning Toolbox."

  

# Prompt:  give the matlab code to read the fileName = 'D:\0lrn\23SP\SPD\LDR\dat\GROUP1\a2361216.333360';. DO NOT read the header lines. The header lines (ASCII format) have the two last characters <CRLF>. The header lines are followed by the data in binary format and 4-bits. 它一共有五组数据第一组4000个，每个4字节第一组结束以后有两个字节是’/r/n’然后接下一组五组分别是4000，2000，4000，2000，4000每个文件有五组. use English notations in the matlab code.


# Read nc  

% Specify the NetCDF file name

filename = 'fx2000_ne120pg3L273_tonga.005.cam.h1.0001-01-20-44400_cdf4.nc';

  

% Open the NetCDF file

ncid = netcdf.open(filename, 'NOWRITE');

  

% Define variable names

varNames = {'hyam', 'hybm', 'ilev', 'hyai', 'hybi'};

  

% Loop through each variable

for i = 1:length(varNames)

    % Read the variable data

    var = netcdf.getVar(ncid, netcdf.inqVarID(ncid, varNames{i}));

    % Read attributes

    long_name = netcdf.getAtt(ncid, netcdf.inqVarID(ncid, varNames{i}), 'long_name');

    units = netcdf.getAtt(ncid, netcdf.inqVarID(ncid, varNames{i}), 'units');

    % Create a new subfigure

    subplot(length(varNames), 1, i);

    % Plot the variable

    plot(var);

    % Set title and ylabel based on attributes

    title(long_name);

    ylabel(units);

    % Add grid and axis labels

    grid on;

    xlabel('Index');

    % Add extra space between subfigures

    if i < length(varNames)

        spacing = 0.05; % Adjust this value as needed

        set(gca, 'Position', get(gca, 'Position') + [0, spacing, 0, 0]);

    end

end

% Close the NetCDF file

netcdf.close(ncid);
