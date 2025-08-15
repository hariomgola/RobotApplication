const robot = require('robotjs');
const chalk = require('chalk');
const data = require('../data/default.json')


let mouse = robot.getMousePos();

const mouse_x = mouse.x;
let mouseChangeFlag = false;

console.log(process.args)
const changeMouse = (timedelay = data.timedelay,TimeinMS=data.TimeinMS) => {
    console.log(chalk.magenta(` -  Current mouse position ${JSON.stringify(mouse)} -`))
    robot.setMouseDelay(timedelay)
    for(let i=0;i<TimeinMS;i++){
        console.clear();
        console.log(chalk.cyan('-----------------------------------------------------'))
        if(mouseChangeFlag){
            break;
        }
        if(i%data.MultipleCheck==0){
            console.log(chalk.yellow(`      - changing mouse position to x:${mouse.x}, y:${mouse.y+data.MouseMove} -   `));
            robot.moveMouseSmooth(mouse.x,mouse.y+data.MouseMove);
            mouse = robot.getMousePos();
        }else{
            console.log(chalk.yellow(`      - changing mouse position to x:${mouse.x}, y:${mouse.y-data.MouseMove} -    `));
            robot.moveMouseSmooth(mouse.x,mouse.y-data.MouseMove);
            mouse = robot.getMousePos();
        }
        killTerminalMouseMove();
        console.log(chalk.cyan('------------------------------------------------------'))
    }
    copyRight();
}

const killTerminalMouseMove = () =>{
    // checking wheather mouse change its position (online)
    if(mouse.x!=mouse_x){
        mouseChangeFlag = true;
    }
}

const copyRight = () =>{
    console.clear();
    console.log(chalk.green(` * -Thanks for coming online its been very difficult to keep your pc awake - *`))
    console.log(chalk.cyan.bold.italic(data.copyright))
    console.log(chalk.green.bold.italic(`love this project <3 follow -${data.follow}`))
}

changeMouse(100,500);