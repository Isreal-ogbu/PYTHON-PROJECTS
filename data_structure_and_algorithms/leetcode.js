// practise question

var countSubIslands = function(grid1, grid2) {
    
    // grid1[r][c] and grid2[r][c] both same and 0 return 1
    // otherwise 0
    // r>rows or r<0 outof boundry return 1
    // if all directions dfs are 1 return 1 else 0
    // start dfs when grid2[r][c] == 1
    const rows= grid1.length;
    const cols = grid1[0].length;
    
    let noOfSubIslands = 0;
    for(let r=0;r<rows; r++){
        for(let c=0;c<cols; c++){
            if(grid2[r][c] === 1 && dfs(grid1, grid2, r, c)){
                noOfSubIslands +=1;
            }
        }
    }
    
    return noOfSubIslands;
};

function dfs(grid1, grid2, r, c){
    const rows= grid1.length;
    const cols = grid1[0].length;
    if(r < 0 || r>=rows || c<0 || c>= cols){
        return 1
    }
    if(grid2[r][c] === 0) return 1;
    if(grid2[r][c] !== grid1[r][c]){
        return 0;
    }
    
    grid2[r][c] = 0;
    grid1[r][c] = 0;
    const top = dfs(grid1, grid2, r-1, c);
    const right = dfs(grid1, grid2, r, c+1);
    const bottom = dfs(grid1, grid2, r+1, c);
    const left = dfs(grid1, grid2, r, c-1);
    if(top ===0 || right === 0 || bottom === 0 || left === 0){
        return 0;
    }
    return 1; 
    
}