% This code is a result of my (Sarah Morgan's) SM thesis here: [[3]](#3). Several case studies are shown there with a more in-depth discussion of this procedure of adaptable maneuver planning. 
% © Massachusetts Institute of Technology 2021.
% Thank you to Matthew Moraguez for assistance with this script!


function varargout = mobile_target_gui(varargin)
% MOBILE_TARGET_GUI MATLAB code for mobile_target_gui.fig
%      MOBILE_TARGET_GUI, by itself, creates a new MOBILE_TARGET_GUI or raises the existing
%      singleton*.
%
%      H = MOBILE_TARGET_GUI returns the handle to a new MOBILE_TARGET_GUI or the handle to
%      the existing singleton*.
%
%      MOBILE_TARGET_GUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MOBILE_TARGET_GUI.M with the given input arguments.
%
%      MOBILE_TARGET_GUI('Property','Value',...) creates a new MOBILE_TARGET_GUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before mobile_target_gui_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to mobile_target_gui_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help mobile_target_gui

% Last Modified by GUIDE v2.5 13-May-2021 18:07:25

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @mobile_target_gui_OpeningFcn, ...
                   'gui_OutputFcn',  @mobile_target_gui_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before mobile_target_gui is made visible.
function mobile_target_gui_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to mobile_target_gui (see VARARGIN)

%Add esl logo
axes(handles.logos);
eslLogo = imread('esl_logo.png');
image(eslLogo);
axis off
axis image

%Add plot
load matlab.mat
axes(handles.nondominated_plot);
pointsize = 25;
x2 = table2array(outputga97singlesatF(:,1))
x2(~any(~isnan(x2),2),:)=[]
y2 = table2array(outputga97singlesatF(:,2))*10
y2(~any(~isnan(y2),2),:)=[]
z2 = table2array(outputga97singlesatF(:,3))
z2(~any(~isnan(z2),2),:)=[]
handles.nondominated_plot =scatter(x2, z2, pointsize, -y2, 'filled', 'MarkerEdgeColor', [0,0,0])
xlabel('Total Delta-V Used (m/s)')
ylabel('Mean Distance to Targets Accessed (km)')
h = colorbar;
ylabel(h, 'Total Target Access Time (s)')
%plot = imread('harvey_1.jpg');
%image(plot);
%axis off
%axis image

% Choose default command line output for mobile_target_gui
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes mobile_target_gui wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = mobile_target_gui_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in run_opt.
function run_opt_Callback(hObject, eventdata, handles)
% hObject    handle to run_opt (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



function thrust_Callback(hObject, eventdata, handles)
% hObject    handle to thrust (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of thrust as text
%        str2double(get(hObject,'String')) returns contents of thrust as a double


% --- Executes during object creation, after setting all properties.
function thrust_CreateFcn(hObject, eventdata, handles)
% hObject    handle to thrust (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function mass_Callback(hObject, eventdata, handles)
% hObject    handle to mass (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mass as text
%        str2double(get(hObject,'String')) returns contents of mass as a double


% --- Executes during object creation, after setting all properties.
function mass_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mass (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function alt_Callback(hObject, eventdata, handles)
% hObject    handle to alt (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of alt as text
%        str2double(get(hObject,'String')) returns contents of alt as a double


% --- Executes during object creation, after setting all properties.
function alt_CreateFcn(hObject, eventdata, handles)
% hObject    handle to alt (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function incl_Callback(hObject, eventdata, handles)
% hObject    handle to incl (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of incl as text
%        str2double(get(hObject,'String')) returns contents of incl as a double


% --- Executes during object creation, after setting all properties.
function incl_CreateFcn(hObject, eventdata, handles)
% hObject    handle to incl (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function greenwich_epoch_Callback(hObject, eventdata, handles)
% hObject    handle to greenwich_epoch (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of greenwich_epoch as text
%        str2double(get(hObject,'String')) returns contents of greenwich_epoch as a double


% --- Executes during object creation, after setting all properties.
function greenwich_epoch_CreateFcn(hObject, eventdata, handles)
% hObject    handle to greenwich_epoch (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function arg_epoch_Callback(hObject, eventdata, handles)
% hObject    handle to arg_epoch (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of arg_epoch as text
%        str2double(get(hObject,'String')) returns contents of arg_epoch as a double


% --- Executes during object creation, after setting all properties.
function arg_epoch_CreateFcn(hObject, eventdata, handles)
% hObject    handle to arg_epoch (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function epoch_month_Callback(hObject, eventdata, handles)
% hObject    handle to epoch_month (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of epoch_month as text
%        str2double(get(hObject,'String')) returns contents of epoch_month as a double


% --- Executes during object creation, after setting all properties.
function epoch_month_CreateFcn(hObject, eventdata, handles)
% hObject    handle to epoch_month (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function raan_epoch_Callback(hObject, eventdata, handles)
% hObject    handle to raan_epoch (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of raan_epoch as text
%        str2double(get(hObject,'String')) returns contents of raan_epoch as a double


% --- Executes during object creation, after setting all properties.
function raan_epoch_CreateFcn(hObject, eventdata, handles)
% hObject    handle to raan_epoch (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function epoch_day_Callback(hObject, eventdata, handles)
% hObject    handle to epoch_day (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of epoch_day as text
%        str2double(get(hObject,'String')) returns contents of epoch_day as a double


% --- Executes during object creation, after setting all properties.
function epoch_day_CreateFcn(hObject, eventdata, handles)
% hObject    handle to epoch_day (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function epoch_year_Callback(hObject, eventdata, handles)
% hObject    handle to epoch_year (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of epoch_year as text
%        str2double(get(hObject,'String')) returns contents of epoch_year as a double


% --- Executes during object creation, after setting all properties.
function epoch_year_CreateFcn(hObject, eventdata, handles)
% hObject    handle to epoch_year (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function num_targets_Callback(hObject, eventdata, handles)
% hObject    handle to num_targets (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of num_targets as text
%        str2double(get(hObject,'String')) returns contents of num_targets as a double


% --- Executes during object creation, after setting all properties.
function num_targets_CreateFcn(hObject, eventdata, handles)
% hObject    handle to num_targets (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function interval_targets_Callback(hObject, eventdata, handles)
% hObject    handle to interval_targets (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of interval_targets as text
%        str2double(get(hObject,'String')) returns contents of interval_targets as a double


% --- Executes during object creation, after setting all properties.
function interval_targets_CreateFcn(hObject, eventdata, handles)
% hObject    handle to interval_targets (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in hurricane_file.
function hurricane_file_Callback(hObject, eventdata, handles)
% hObject    handle to hurricane_file (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



function epoch_hour_Callback(hObject, eventdata, handles)
% hObject    handle to epoch_hour (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of epoch_hour as text
%        str2double(get(hObject,'String')) returns contents of epoch_hour as a double


% --- Executes during object creation, after setting all properties.
function epoch_hour_CreateFcn(hObject, eventdata, handles)
% hObject    handle to epoch_hour (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function epoch_min_Callback(hObject, eventdata, handles)
% hObject    handle to epoch_min (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of epoch_min as text
%        str2double(get(hObject,'String')) returns contents of epoch_min as a double


% --- Executes during object creation, after setting all properties.
function epoch_min_CreateFcn(hObject, eventdata, handles)
% hObject    handle to epoch_min (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function epoch_sec_Callback(hObject, eventdata, handles)
% hObject    handle to epoch_sec (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of epoch_sec as text
%        str2double(get(hObject,'String')) returns contents of epoch_sec as a double


% --- Executes during object creation, after setting all properties.
function epoch_sec_CreateFcn(hObject, eventdata, handles)
% hObject    handle to epoch_sec (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
