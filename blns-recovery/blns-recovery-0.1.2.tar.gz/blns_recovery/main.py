import argparse
import binascii

from mnemonic import Mnemonic

from blns_recovery.mnemo import BlnsMnemonic
from blns_recovery.recovery import recover_seed, bitcoin_seed


def main():
    parser = argparse.ArgumentParser(description='blns paper backup recovery')

    parser.add_argument('--part1', dest='part1', default=None,
                        help='Part 1 of the paper backup')
    parser.add_argument('--part2', dest='part2', default=None,
                        help='Part 2 of the paper backup')
    parser.add_argument('--part1-hex', dest='part1_hex', default=None,
                        help='Part 1 of the paper backup in the hexadecimal form')
    parser.add_argument('--part2-hex', dest='part2_hex', default=None,
                        help='Part 2 of the paper backup in the hexadecimal form')
    parser.add_argument('--bip-language', dest='bip_language', default='english',
                        help='BIP39 mnemonic language to use')
    parser.add_argument('--show-btc-secret', dest='show_btc_secret', action='store_const', const=True,
                        help='Show BTC master private keys')
    args = parser.parse_args()

    part1, part2 = None, None
    mnemonic = BlnsMnemonic()
    bip_mnemonic = Mnemonic(args.bip_language)

    if args.part1:
        part1 = mnemonic.to_binary(args.part1)
    elif args.part1_hex:
        part1 = binascii.unhexlify(args.part1_hex)
    else:
        print('Error: Part1 of the BLNS paper backup is not specified')
        return

    if args.part2:
        part2 = mnemonic.to_binary(args.part2)
    elif args.part2_hex:
        part2 = binascii.unhexlify(args.part2_hex)
    else:
        print('Error: Part2 of the BLNS paper backup is not specified')
        return

    seed = recover_seed(part1, part2)
    seed_mnemo = bip_mnemonic.to_mnemonic(seed)
    print('Recovered master seed: %s\nBIP-39 mnemonic: %s' % (binascii.hexlify(seed).decode('utf8'), seed_mnemo))

    if args.show_btc_secret:
        btc_priv, btc_chain = bitcoin_seed(seed)
        print('BTC master private key: %s, chain code: %s'
              % (binascii.hexlify(btc_priv).decode('utf8'), binascii.hexlify(btc_chain).decode('utf8')))


if __name__ == '__main__':
    main()
