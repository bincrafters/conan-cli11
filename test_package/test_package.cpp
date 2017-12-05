#include "CLI/CLI.hpp"

int main(int argc, char **argv)
{
    CLI::App app("K3Pi goofit fitter");
    CLI11_PARSE(app, argc, argv);
}
