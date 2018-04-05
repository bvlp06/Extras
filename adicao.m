function varargout = adicao(varargin)
% ADICAO MATLAB code for adicao.fig
%      ADICAO, by itself, creates a new ADICAO or raises the existing
%      singleton*.
%
%      H = ADICAO returns the handle to a new ADICAO or the handle to
%      the existing singleton*.
%
%      ADICAO('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in ADICAO.M with the given input arguments.
%
%      ADICAO('Property','Value',...) creates a new ADICAO or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before adicao_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to adicao_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help adicao

% Last Modified by GUIDE v2.5 08-Aug-2017 18:46:42

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @adicao_OpeningFcn, ...
                   'gui_OutputFcn',  @adicao_OutputFcn, ...
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


% --- Executes just before adicao is made visible.
function adicao_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to adicao (see VARARGIN)

% Choose default command line output for adicao
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes adicao wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = adicao_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function valor2_Callback(hObject, eventdata, handles)
% hObject    handle to valor2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.numero2 = str2double(get(hObject,'String'));
guidata(hObject,handles);

% Hints: get(hObject,'String') returns contents of valor2 as text
%        str2double(get(hObject,'String')) returns contents of valor2 as a double


% --- Executes during object creation, after setting all properties.
function valor2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to valor2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function valor1_Callback(hObject, eventdata, handles)
% hObject    handle to valor1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.numero1 = str2double(get(hObject,'String'));
guidata(hObject,handles);

% Hints: get(hObject,'String') returns contents of valor1 as text
%        str2double(get(hObject,'String')) returns contents of valor1 as a double


% --- Executes during object creation, after setting all properties.
function valor1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to valor1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in resolver.
function resolver_Callback(hObject, eventdata, handles)
% hObject    handle to resolver (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
resultado = handles.numero1 + handles.numero2;
   set(handles.resultado,'FontSize',26);
   set(handles.resultado,'String',resultado);
