int solution(int A[], int N) {
    int candidate;
    int count = 0;
    int i;
    // 1. Find most likely candidate for the leader
    for(i = 0; i < N; i++){
        // change candidate when count reaches 0
        if(count == 0) candidate = i;
        // count occurrences of candidate
        if(A[i] == A[candidate]) count++;
        else count--;
    }
    // 2. Verify that candidate occurs more than N/2 times
    count = 0;
    for(i = 0; i < N; i++) if(A[i] == A[candidate]) count++;
    // If there's no leader then that there are also no equi-leaders
    if (count <= N/2) return 0;
    // 3. There exists a leader now count the number of occurences
    // of this leader in all sequences.
    int leader = A[candidate];
    int equiLeaderCount = 0;
    int cntL = 0; // leader count for the left sequence
    int cntR = count; // leader count for the right sequence
    for(int i = 0; i < N-1; i++){
        if(A[i] == leader){
            cntL++;
            cntR--;
        }
        // verify that the dominant value in both sequences
        // is the same
        if(cntL > (i+1)/2 && cntR > (N-i-1)/2) equiLeaderCount++;
    }
    return equiLeaderCount;
}
