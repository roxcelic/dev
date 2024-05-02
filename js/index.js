//checks for touch support as i am unsure on how to check for a physical keybord
var supportsTouch = ("ontouchstart" in window) || window.navigator.msMaxTouchPoints > 0;
if (supportsTouch){
    script_identi.innerHTML = "";
    const NMainCont = document.createElement("div");
    script_identi.appendChild(NMainCont);
    NMainCont.id = "roxcelic-type-main";
    NMainCont.style.backgroundColor = "black";
    NMainCont.style.height = script_height;
    NMainCont.style.width = script_width;
    NMainCont.style.borderRadius = "5px";
    NMainCont.style.color = "white";
    NMainCont.style.position = "relative";
    NMainCont.style.overflow = "hidden";
    NMainCont.style.fontFamily = "Pixelify Sans";
    NMainCont.style.textAlign = "center";
    NMainCont.innerText = "sorry but no";
}

//variables and such
let script_identi = document.currentScript.getAttribute('id');
let script_width = document.currentScript.getAttribute('width');
let script_height = document.currentScript.getAttribute('height');
let script_box_height = document.currentScript.getAttribute('box-height');
let script_padding_base = document.currentScript.getAttribute('padding-base');
let script_padding_alt = document.currentScript.getAttribute('padding-alt');
let script_link = document.currentScript.getAttribute('link');

let Info = {
    INTRO: [
        "welcome to my fun funky and cool js thing...",
        "im gonna be honest not even im sure why i made a js version of my weird python thing",
        "it doesnt do much now but i guess it could do much more",
        "run '?help' if you need assistance"
    ],
    ERROR: "nuh uh uh",
    INVALID_COMMAND: "invalid command",
    COMMANDS: [
        ["?help","prints all availible commands"],
        [".credits","runs the credits"],
        [".clear","clears the terminal"],
        [".intro","replays the intro"],
        [".fullscreen","fullscreens the terminal"],
        [".change_link","changes the link that the page changes to when ended"],
        [".end","ends the script (redirects to the page described in the script tag)"]
    ],
    CREDITS:[
        ["roxie","i am the idiot mostly responsible for this"],
        ["Martha ","the genius who helped me"]
    ]
}

canType = true;

function NewLine(text){
    let newLine = document.createElement("p");
    newLine.textContent = " - " + text;
    newLine.style.margin = "0";
    newLine.style.paddingLeft = script_box_height;
    ThriCont.appendChild(newLine);
    ThriCont.scrollTo(0, ThriCont.scrollHeight);
}

function PrintLine(pLine){
    let print = document.createElement("p");
    print.textContent = pLine;
    print.style.margin = "0";
    print.style.paddingLeft = script_padding_base;
    ThriCont.appendChild(print);
    ThriCont.scrollTo(0, ThriCont.scrollHeight);
}

//importing the font it uses
function addFontLink(rel, href){
    let Link = document.createElement("link");
    Link.rel = rel;
    Link.href = href;
    document.head.appendChild(Link);
}
addFontLink("preconnect","https://fonts.googleapis.com");
addFontLink("preconnect","https://fonts.gstatic.com");
addFontLink("stylesheet","https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400..700&display=swap");

//sets the main element to the script itself
script_identi = document.getElementById(script_identi);
script_identi.style.display = "block";

//making a div element for the roxcelic-type-main element (the main element)
const MainCont = document.createElement("div");
script_identi.appendChild(MainCont);
MainCont.id = "roxcelic-type-main";

//making the main outline of the 'terminal'
if (MainCont.style.backgroundColor == ""){
    MainCont.style.backgroundColor = "black";
    MainCont.style.height = script_height;
    MainCont.style.width = script_width;
    MainCont.style.borderRadius = "5px";
    MainCont.style.color = "white";
    MainCont.style.position = "relative";
    MainCont.style.overflow = "hidden";
    MainCont.style.fontFamily = "Pixelify Sans";
    MainCont.style.resize = "both";
}

//now that the main box has been made id like to make 2 elements
//one which will contain the input feild which will manage inputs via an event listener
//and a backlog of text which will act as the terminal

const SecCont = document.createElement("div");
MainCont.appendChild(SecCont);
SecCont.id = "roxcelic-type-alt-1";

if (SecCont.style.backgroundColor == ""){
    SecCont.style.backgroundColor = "black";
    SecCont.style.height = script_box_height;
    SecCont.style.width = script_width;
    SecCont.style.color = "white";
    SecCont.style.position = "absolute";
    SecCont.style.bottom = "0";
    SecCont.style.paddingLeft = script_padding_alt;
    SecCont.textContent = "_"
}

//now ill make the element which acts as a backlog
const ThriCont = document.createElement("div");
MainCont.appendChild(ThriCont);
ThriCont.id = "roxcelic-type-alt-2";

if (ThriCont.style.backgroundColor == ""){
    ThriCont.style.backgroundColor = "black";
    ThriCont.style.height = "calc(100% - " + script_box_height + ")";
    ThriCont.style.width = script_width;
    ThriCont.style.color = "white";
    ThriCont.style.position = "absolute";
    ThriCont.style.top = "0";
    ThriCont.style.overflowY = "scroll";
    ThriCont.style.scrollbarColor = "white transparent";
    ThriCont.style.scrollbarWidth = "thin";
}

//here is the start
for (item in Info.INTRO){
    PrintLine(Info.INTRO[item]);
}

//the typing function using the event listener previously discussed
const inputField = document.querySelector("html");
inputField.addEventListener("keydown", async (e) => {
    if (canType){
        if (e.key == "Enter"){
            NewLine(SecCont.textContent.slice(0, -1));

            let tet = SecCont.textContent.slice(0, -1);

            const args = SecCont.textContent.trim().split(" ");
            const commandName = args.shift().toLowerCase().slice(0, -1);

            SecCont.textContent = "_";

            const command = commands.find((c) => c.name === commandName);
            if (!command) return await PrintLine(Info.INVALID_COMMAND);

            try {
                await command.execute(args);
            } catch(err) {
                await PrintLine(Info.ERROR);
            }

        }
        else if (e.key == "Backspace"){
            SecCont.textContent = SecCont.textContent.slice(0, -2);
            SecCont.textContent = SecCont.textContent + "_";
        }
        else{
            if(e.key.length == 1){
                SecCont.textContent = SecCont.textContent.slice(0, -1) + e.key;
                SecCont.textContent = SecCont.textContent + "_";
            }
        }
    }
});

//here are the commands, feel welcome to mess or add some
const commands = [
    {
        name: "?help",
        execute: async () => {
            for (item in Info.COMMANDS){
                PrintLine(Info.COMMANDS[item][0] + " - " + Info.COMMANDS[item][1]);
            }
        },
    },
    {
        name: ".end",
        execute: async () => {
            window.location.href = script_link;
        },
    },
    {
        name: ".credits",
        execute: async () => {
            for (item in Info.CREDITS){
                PrintLine(Info.CREDITS[item][0] + " - " + Info.CREDITS[item][1]);
            }
        },
    },
    {
        name: ".clear",
        execute: async () => {
            ThriCont.innerHTML = "";
        },
    },
    {
        name: ".intro",
        execute: async () => {
            for (item in Info.INTRO){
                PrintLine(Info.INTRO[item]);
            }
        },
    },
    {
        name: ".fullscreen",
        execute: async () => {
            MainCont.requestFullscreen();
        },
    },
    {
        name: ".change_link",
        execute: async () => {
            let person = prompt("Please enter the new link", script_link);
            if (person == null || person === "") {
                PrintLine("you denied the prompt");
            } else {
                script_link = person;
                PrintLine("the link to the end has been changed to " + script_link);
                PrintLine("please remeber if the link was entered incorrectly it may cause an error");
            }
        },
    },
    {
        name: "what",
        execute: async () => {
            PrintLine("let it begin");
            setInterval(function(){
                PrintLine("AHHHHHHHHH");
            }, 20)
        },
    },
    {
        name: "strange-glove",
        execute: async () => {
            setInterval( async() =>{
                await print();
            }, 20)
        },
    },
    {
        name: "snivey",
        execute: async () => {
            navigator.clipboard.writeText("cockwomble");
        },
    },
]