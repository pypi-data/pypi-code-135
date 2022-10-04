import math
import itertools as it
from requests import HTTPError
from requests import ReadTimeout
from web3 import exceptions
import time

from dexhub.dex import UniswapV2
#useful tool for dex
class DexHelper:

    ################################################
    #   optimal trade volume
    ################################################
    #   This is a implement of optimal trade volume,
    #   please reffer to 
    #       https://arxiv.org/pdf/2105.02784.pdf  
    #   for more math detail,
    ################################################

    #uniswap swap fee
    r1=0.997
    r2=1

    #update swap fee based on the protocol
    def set_r1(self,_r1):
        self.r1=_r1

    def set_r2(self,_r2):
        self.r2=_r2

    #trianglular arbitrage optimal volume
    # arbitrage route 1->2->3->1
    # a12 is the token1 reserve volume in token pair 1-2
    def optimal_volume_triangle(self,_a12,_a21,_a23,_a32,_a31,_a13):
        a13_prime=self.get_a13_prime(_a12,_a21,_a23)
        a31_prime=self.get_a31_prime(_a21,_a32,_a23)
        a=self.get_a(a13_prime,_a31,a31_prime)
        a_prime=self.get_a_prime(_a13,a31_prime,_a31)
        denominator=(1+math.isqrt(int(self.r1*self.r2*a_prime*a-1))-a)
        return denominator/self.r1

    #trianglular arbitrage optimal volume
    # arbitrage route 1->2->3->4->1
    # a12 is the token1 reserve volume in token pair 1-2
    def optimal_volume_quadrilateral(self,_a12,_a21,_a23,_a32,_a34,_a43,_a41,_a14):
        #convert _a12 _a21 _a23 _a32 to _a13 _a31
        _a13=self.get_a13_prime(_a12,_a21,_a23)
        _a31=self.get_a31_prime(_a21,_a32,_a23)
        #1341 volume calculate        
        return self.optimal_volume_triangle(_a13,_a31,_a34,_a43,_a41,_a14)


    # general optiimal volume function
    # artbitrage route 1->2->3->...->n->1
    def optimal_volume(self,reserves:list):
        list_length=len(reserves)
        assert(list_length%2==0)
        assert(list_length>=6)
        if list_length>6:
            for i in range(int(list_length/2-3)):
                _a13=self.get_a13_prime(reserves[0],reserves[1],reserves[2])
                _a31=self.get_a31_prime(reserves[1],reserves[3],reserves[2])
                del reserves[3]
                del reserves[2]
                reserves[0]=_a13
                reserves[1]=_a31
        assert(len(reserves)==6)
        return self.optimal_volume_triangle(reserves[0],reserves[1],reserves[2],reserves[3],reserves[4],reserves[5])

    def get_a(self,_a13_prime,_a31,_a31_prime):
        return int(_a13_prime*_a31/(_a31+self.r1*self.r2*_a31_prime))

    def get_a_prime(self,_a13,_a31_prime,_a31):
        return int((self.r1*self.r2*_a13*_a31_prime)/(_a31+self.r1*self.r2*_a31_prime))
    
    def get_a13_prime(self,_a12,_a21,_a23):
        return int(_a12*_a23/(_a23+self.r1*self.r2*_a21))
        
    def get_a31_prime(self,_a21,_a32,_a23):
        return int(self.r1*self.r2*_a21*_a32/(_a23+self.r1*self.r2*_a21))


    ################################################
    #   prepair the pair list and path list 
    #   for arbitrage bot
    ################################################
    #
    #
    ################################################

    def get_pair_list_and_path_list(self,_arbitrage_token:str,_token_list:list,_dex:UniswapV2):
        # save the pair tokens address with reserve
        pair_list=[]
        # save the path which is available to arbitrage
        path_list=[]

        #get pair list
        for token in _token_list:
            if (_dex.get_pair(_arbitrage_token,token)!="0x0000000000000000000000000000000000000000"):
                pair_list.append([_arbitrage_token,token])
        pair_combination=it.combinations(_token_list,2)
        for pair in pair_combination:
            #make sure all the pair exist
            flag_pair0_pair1=_dex.get_pair(pair[0],pair[1])!="0x0000000000000000000000000000000000000000"
            if (flag_pair0_pair1):
                pair_list.append([pair[0],pair[1]])

        #get path list
        pair_permutation=it.permutations(_token_list,2)
        for pair in pair_permutation:
            flag_pair0_pair1=_dex.get_pair(pair[0],pair[1])!="0x0000000000000000000000000000000000000000"
            flag_pair0_token=_dex.get_pair(pair[0],_arbitrage_token)!="0x0000000000000000000000000000000000000000"
            flag_pair1_token=_dex.get_pair(pair[1],_arbitrage_token)!="0x0000000000000000000000000000000000000000"
            if (flag_pair0_pair1 and flag_pair0_token and flag_pair1_token):
                path_list.append([_arbitrage_token,pair[0],pair[1],_arbitrage_token])
        tri_pair_permutation=it.permutations(_token_list,3)
        for pair in tri_pair_permutation:
            flag_pair0_pair1=_dex.get_pair(pair[0],pair[1]) !="0x0000000000000000000000000000000000000000"
            flag_pair1_pair2=_dex.get_pair(pair[1],pair[2]) !="0x0000000000000000000000000000000000000000"
            flag_pair0_token=_dex.get_pair(pair[0],_arbitrage_token) !="0x0000000000000000000000000000000000000000"
            flag_pair2_token=_dex.get_pair(pair[2],_arbitrage_token) !="0x0000000000000000000000000000000000000000"
            if ( flag_pair0_pair1 and flag_pair1_pair2 and flag_pair0_token and flag_pair2_token):
                path_list.append([_arbitrage_token,pair[0],pair[1],pair[2],_arbitrage_token])
        return pair_list,path_list

    def get_pair_reserve_dict(self,_pair_list:list,_dex:UniswapV2):
        # save the token0token1   ----    reserve0,reserve1 dictionary
        pair_reserve_dict={}
        for pair in _pair_list:
            pair_address=_dex.get_pair(pair[0],pair[1])
            token0Address,reserve0,token1Address,reserve1,blockTimeStamp,price0,price1=_dex.get_pair_info(pair_address)
            key=token0Address+token1Address
            pair_reserve_dict[str(key)]=[pair_address,reserve0,reserve1]
        return pair_reserve_dict

    #throw except if fail to find the reserve which should not happen
    #return list of reserves in order of a12 a21 a23 a32 ... a(n-1)(n)  a(n)(n-1)   a(n)(1)  a(1)(n)    
    def path_to_reserve(self,_path:list,_pair_reserve_dict):
        reserve_list=[]
        for i in range(len(_path)-1):
            try:
                address,a01,a10=_pair_reserve_dict[(_path[i]+_path[i+1])]
            except KeyError as k:
                address,a10,a01=_pair_reserve_dict[(_path[i+1]+_path[i])]
            assert(a01>50000)
            assert(a10>50000)
            reserve_list.append(a01)
            reserve_list.append(a10)
        return reserve_list

    #return int, if result >0, there is arbitrage chance
    def get_arbitrage_space(self,_reserve_list:list,_ex_rate):
        assert(len(_reserve_list)%2==0)
        p=1
        for i in range(int(len(_reserve_list)/2)):
            p=p*(_reserve_list[i*2+1]/_reserve_list[i*2])*_ex_rate
        return p-1


    #arbitrage swap function
    def swap(self,_dex:UniswapV2,_amountIn,_amountOut,_path:list,_to_address,_deadline,_gas):
        try:
            _dex.swapExactTokenForTokensWithGasWithNonce(_amountIn,_amountOut,_path,_to_address,_deadline,600000,_dex.nonce)
            _dex.nonce+=1
        except exceptions.ContractLogicError as e:
            print(e)
        except exceptions.ValidationError as e:
            print(e)
        except ReadTimeout as e:
            print(e)
        except HTTPError as e:
            print(e)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except:
            print("####################################")
            print("################error###############")
            print("####################################")
            time.sleep(2)
